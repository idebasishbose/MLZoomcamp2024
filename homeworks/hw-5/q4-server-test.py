import requests
from rich import print


url = "http://localhost:9670/predict"

client = {"job": "student", "duration": 280, "poutcome": "failure"}
response = requests.post(url, json=client).json()
print(response)
