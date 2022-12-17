import requests 
from datetime import datetime


USERNAME = "notzarif"
TOKEN = "Azazazazazazaz7"
GRAPH_ID = "notzarifgraph1"

today = datetime.now()
pixela_endpoint = "https://pixe.la/v1/users"

## Creating pixela account ##
pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)

## Creating graph ##
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
}

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=graph_headers)

## Inputing data in graph ##
data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

data_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

data_header = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(
    url=data_endpoint, headers=data_header, json=data_params)

