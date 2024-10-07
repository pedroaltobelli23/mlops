import requests
import json

# Change the endpoint
url_endpoint = "https://6qphx0oije.execute-api.us-east-2.amazonaws.com"

url = f"{url_endpoint}/predict"

# Change the phrase
body = {"age": 42,"job": "entrepreneur","marital": "married","education": "primary","balance": 558,"housing": "yes","duration": 15,"campaign": 2}
resp = requests.post(url,json=body)
print(f"status code: {resp.status_code}")
print(f"text: {resp.text}")