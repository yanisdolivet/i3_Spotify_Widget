import requests
import base64

client_id = 
client_secret = 
auth_code = 
redirect_uri = 

# Prepare headers and data for the POST request
auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode("utf-8")
headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": redirect_uri
}

# Make the request
response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

# Check if request was successful
if response.status_code == 200:
    tokens = response.json()
    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)
else:
    print("Error:", response.status_code, response.json())
