import requests

client_id = "your_client_id"
client_secret = "your_client_secret"

def get_access_token():
    url = "https://login.procore.com/oauth/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Access token received!")
        return response.json()["access_token"]
    else:
        print("Error getting token:", response.json())
        return None

if __name__ == "__main__":
    access_token = get_access_token()
    print("Access Token:", access_token)
