import os
import requests

def get_access_token():
    url = "https://login.procore.com/oauth/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("PROCORE_CLIENT_ID"),
        "client_secret": os.getenv("PROCORE_CLIENT_SECRET"),
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Error fetching access token: {response.json()}")
