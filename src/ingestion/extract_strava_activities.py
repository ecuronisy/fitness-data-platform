import json
import os
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv

load_dotenv("config/.env")

METADATA_FILE = "data/metadata/strava_ingestion_state.json"

# --------------------------------------------------
# Get Access Token
# --------------------------------------------------

token_response = requests.post(
    "https://www.strava.com/oauth/token",
    data={
        "client_id": os.getenv("STRAVA_CLIENT_ID"),
        "client_secret": os.getenv("STRAVA_CLIENT_SECRET"),
        "refresh_token": os.getenv("STRAVA_REFRESH_TOKEN"),
        "grant_type": "refresh_token",
    },
    verify=False,
)

token_response.raise_for_status()

access_token = token_response.json()["access_token"]

print("Access token obtained successfully")

# --------------------------------------------------
# Read metadata
# --------------------------------------------------

with open(METADATA_FILE, "r", encoding="utf-8") as file:
    metadata = json.load(file)

last_activity_date = metadata["last_activity_date"]

dt = datetime.strptime(
    last_activity_date,
    "%Y-%m-%dT%H:%M:%SZ"
)

after_timestamp = int(
    dt.replace(tzinfo=timezone.utc).timestamp()
)

# --------------------------------------------------
# Download only new activities
# --------------------------------------------------

activities_response = requests.get(
    "https://www.strava.com/api/v3/athlete/activities",
    headers={
        "Authorization": f"Bearer {access_token}"
    },
    params={
        "after": after_timestamp
    },
    verify=False,
)

activities_response.raise_for_status()

activities = activities_response.json()

print(f"New activities found: {len(activities)}")

# --------------------------------------------------
# No new activities
# --------------------------------------------------

if len(activities) == 0:
    print("No new activities detected")
    exit()

# --------------------------------------------------
# Save Bronze snapshot
# --------------------------------------------------

output_directory = (
    "data/fitness_catalog/bronze/strava_activities"
)

os.makedirs(output_directory, exist_ok=True)

timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

output_file = os.path.join(
    output_directory,
    f"activities_{timestamp}.json"
)

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(
        activities,
        file,
        indent=4,
        ensure_ascii=False,
    )

print(f"Saved: {output_file}")

# --------------------------------------------------
# Update metadata
# --------------------------------------------------

latest_activity_date = activities[0]["start_date"]

metadata["last_activity_date"] = (
    latest_activity_date
)

with open(
    METADATA_FILE,
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        metadata,
        file,
        indent=4,
        ensure_ascii=False,
    )

print(
    f"Metadata updated: {latest_activity_date}"
)