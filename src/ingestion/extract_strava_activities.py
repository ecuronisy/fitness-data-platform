import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv("config/.env")

# ------------------------------------------------------------------
# Step 1: Get fresh access token
# ------------------------------------------------------------------

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

# ------------------------------------------------------------------
# Step 2: Download activities
# ------------------------------------------------------------------

activities_response = requests.get(
    "https://www.strava.com/api/v3/athlete/activities",
    headers={
        "Authorization": f"Bearer {access_token}"
    },
    params={
        "per_page": 200,
        "page": 1,
    },
    verify=False,
)

activities_response.raise_for_status()

activities = activities_response.json()

print(f"Activities downloaded: {len(activities)}")

# ------------------------------------------------------------------
# Step 3: Create Bronze folder
# ------------------------------------------------------------------

output_directory = (
    "data/fitness_catalog/bronze/strava_activities"
)

os.makedirs(output_directory, exist_ok=True)

# ------------------------------------------------------------------
# Step 4: Save raw JSON snapshot
# ------------------------------------------------------------------

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

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

print(f"Raw snapshot saved: {output_file}")