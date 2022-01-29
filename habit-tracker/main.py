from datetime import datetime
from turtle import update
from urllib import response
import requests
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "henrynugent"
TOKEN = " "
GRAPH_ID= "graph-1"
user_params={
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"




# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_params={
    "id" : "graph-1",
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
# print(today)
pixel_data ={
    "date":today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint,headers=headers)

