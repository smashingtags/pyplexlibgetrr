import requests
import json

# set up API endpoint and access token
base_url = "http://your.plex.server:32400"
token = "your-plex-api-token"

# retrieve user data using API endpoint and access token
headers = {"X-Plex-Token": token}
url = f"{base_url}/status/sessions"
response = requests.get(url, headers=headers)
data = response.json()

# iterate through each user and library to count the number of files
users = data['MediaContainer']['User']
for user in users:
    username = user['title']
    print(f"User: {username}")
    libraries = user['Library']
    for library in libraries:
        library_name = library['title']
        library_key = library['key']
        url = f"{base_url}/library/sections/{library_key}/all"
        response = requests.get(url, headers=headers)
        library_data = response.json()
        file_count = len(library_data['MediaContainer']['Metadata'])
        print(f"\t{library_name}: {file_count} files")
