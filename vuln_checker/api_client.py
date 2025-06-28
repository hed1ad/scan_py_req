import requests
from parser import parse_requirements

def req_api():
    requirements = parse_requirements("requirements.txt")
    url = "https://api.osv.dev/v1/query"
    

    for entry in requirements:
        response = requests.post(url, json=entry)
        print(f"Package: {entry['package']['name']}, Status: {response.status_code}")
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("Response is not valid JSON:", response.text)

if __name__ == "__main__":
    req_api()