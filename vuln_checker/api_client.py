import requests
from parser import parse_requirements

url = "https://api.osv.dev/v1/query"
data = parse_requirements("requirements.txt")

for entry in data:
    response = requests.post(url, json=entry)
    print(f"Package: {entry['package']['name']}, Status: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON:", response.text)

