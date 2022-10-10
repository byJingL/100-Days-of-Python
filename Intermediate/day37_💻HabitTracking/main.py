import requests
from datetime import datetime

# Todo: 1.Create your user account
pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "jennyroh"
TOKEN = "hfjkdfbljuehfie"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Have Created
# response = requests.post(pixela_endpoint, json=user_params)
# print(response, response.text)

# Todo: 2.Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Tracker",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}
header = {
    "X-USER-TOKEN": TOKEN,
}
# Have Created
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response, response.text)

# Todo: 3.visit url: https://pixe.la/v1/users/jennyroh(username)/graphs/graph1(graphid).html

# Todo: 4.Post value to graph
create_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
today = datetime.now()
format_today = today.strftime("%Y%m%d")
print(format_today)
yesterday = datetime(year=2022, month=8, day=31).strftime("%Y%m%d")
print(yesterday)

create_data = {
    "date": format_today,
    "quantity": input("How many hours do you code today? "),
}
response = requests.post(url=create_endpoint, json=create_data, headers=header)
print(response, response.text)

# Todo: 5.Update value to graph --> PUT Requests
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{format_today}"
update_data = {
    "quantity": "6.5",
}
# Have Updated
# response = requests.put(url=update_endpoint, json=update_data, headers=header)
# print(response, response.text)

# Todo: 6.Delete value to graph
delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{format_today}"
# Have Deleted
# response = requests.delete(url=delete_endpoint, headers=header)
# print(response, response.text)
