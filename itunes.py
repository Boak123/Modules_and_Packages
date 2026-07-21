import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Please provide a search term as a command line argument.")

response = requests.get(f"https://itunes.apple.com/search?term={sys.argv[1]}&limit=5")

music = response.json()

for result in music['results']:
    print(result['trackName'])
