import requests
from rich import print


url = "http://localhost:9670/predict"

client = {"job": "management", "duration": 400, "poutcome": "success"}
response = requests.post(url, json=client).json()
print(response)
