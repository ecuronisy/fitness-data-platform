import os
import requests
from dotenv import load_dotenv

load_dotenv("config/.env")

response = requests.post(
    "https://www.strava.com/oauth/token",
    data={
        "client_id": os.getenv("STRAVA_CLIENT_ID"),
        "client_secret": os.getenv("STRAVA_CLIENT_SECRET"),
        "refresh_token": os.getenv("STRAVA_REFRESH_TOKEN"),
        "grant_type": "refresh_token"
    },
    verify=False
)

print(response.status_code)
print(response.json())