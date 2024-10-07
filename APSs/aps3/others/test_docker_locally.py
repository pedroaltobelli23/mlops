import requests
import json

url = "http://localhost:9500/2015-03-31/functions/function/invocations"

body = {"age": 42,"job": "entrepreneur","marital": "married","education": "primary","balance": 558,"housing": "yes","duration": 15,"campaign": 2}

response = requests.post(url, json=body, timeout=2)

response_json = response.json()

print(f"Status code: {response.status_code}")
print("Response:")
print(json.dumps(response_json, indent=4))