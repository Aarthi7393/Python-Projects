import requests
import os
import datetime as dt
proxy= os.environ.get("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy

##TODO Step1: Create a user account in pixe.la
pixela_end_point= "https://pixe.la/v1/users"
TOKEN = os.environ.get("PIXEL_LA_TOKEN")
USERNAME = "pythontest00"
user_param ={
    "token" :TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}

##TODO Step2: Create a graph definition
graph_endpoint = f"{pixela_end_point}/{USERNAME}/graphs"
GRAPH_ID ="graph1"
graph_param ={
    "id": GRAPH_ID,
    "name":"My Studying hours",
    "unit" : "hours",
    "type" : "float",
    "color": "momiji"
}
token_headers ={
    "X-USER-TOKEN": TOKEN,
}

##TODO Step3: Post value to the graph
post_endpoint=f"{graph_endpoint}/{GRAPH_ID}"
today = dt.datetime.today().strftime("%Y-%m-%d")
TODAY = (f"{today.split('-')[0]}"
         f"{today.split('-')[1]}"
         f"{today.split('-')[2]}")

##TODO Step4: Update the value
update_url =f"{post_endpoint}/{TODAY}"


def create_pixel():
    response = requests.post(url = pixela_end_point, json = user_param)
    print(response.text)
    #o/p : {"message":"Success. Let's visit https://pixe.la/@pythontest00 , it is your profile page!","isSuccess":true}

def create_graph():
    response = requests.post(url=graph_endpoint, json = graph_param, headers=token_headers)
    print(response.text)
    #Graph is built : https://pixe.la/v1/users/pythontest00/graphs/graph1.html
def post_value():
    post_param = {
        "date": TODAY,
        "quantity": input("Enter the amount of hours studied today : "),
    }

    response = requests.post(post_endpoint, json=post_param, headers=token_headers)
    print(response.text)

def update_value():
    update_param = {
        "quantity": input("Enter the amount of hours studied today to be updated : "),
    }

    response = requests.put(update_url, json=update_param, headers=token_headers)
    print(response.text)

##TODO Step5: Delete a value
def delete_value():
    response = requests.delete(update_url, headers=token_headers)
    print(response.text)


user_input = input("Enter your choice: post, update, delete: ").lower()
if user_input == "post":
    post_value()
elif user_input == "update":
    update_value()
elif user_input == "delete":
    confirmation = input("Are you sure you want to delete the item for today? (y/n): ")
    if confirmation == "y":
        delete_value()