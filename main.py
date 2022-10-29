import requests
import os
import urllib
import json

bearer_token = os.environ.get("BEARER_TOKEN")
headers = {"Authorization": f"Bearer {bearer_token}"}
query = urllib.parse.quote("ekusiadadus")
url = f'https://api.twitter.com/2/tweets/search/recent?query={query} -is:retweet'
response = requests.get(url, headers=headers)
json_res = response.json()
print(json.dumps(json_res, indent=2, sort_keys=True, ensure_ascii=False))
