import requests
from datetime import datetime
pixela_endpoint="https://pixe.la/v1/users"
Username="abyi"
Token="azsxdcvf78"
user_para={
    "token":Token,
    "username":Username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#respons = requests.post(url=pixela_endpoint,json=user_para)
#print(respons.text)

Graph_endPt=f"{pixela_endpoint}/{Username}/graphs"
graph_Id="graph09"
graph_Name="Coding Graph"

graph_config={
    "id":graph_Id,
    "name":graph_Name,
    "unit":"minute",
    "type":"float",
    "color":"momiji"
}

headers={
    "X-USER-TOKEN":Token
}

#returns=requests.post(url=Graph_endPt,json=graph_config,headers=headers)
#print(returns.text)
today= datetime(year=2023,month=4,day=2)
print(today.strftime("%y%m%d"))
date="20230428"
Pixel_endPt=f"{pixela_endpoint}/{Username}/graphs/{graph_Id}"
pixel_config={
    "date":date,
    "quantity":"69.4",
}
views=requests.post(url=Pixel_endPt,json=pixel_config,headers=headers)
print(views.text)
