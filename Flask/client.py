import requests
import app

url = "http://192.168.0.105:8090/countries"

def get():
    response = requests.get(url)
    print(response.json())

def insert():
    insert = {"name": "Japan", "capital": "Tokyo", "area": 377900}
    response = requests.post(url, json=insert)
    print(response.json())

def get_country_by_id(id):
    url = f"http://192.168.0.105:8090/countries/{id}"
    response = requests.get(url)
    print(response.json())

def update(id):
    update = {"name": "Japan", "capital": "Tokyo", "area": 377975}
    url = f"http://192.168.0.105:8090/countries/{id}"
    response = requests.put(url, json=update)
    print(response.json())

def delete(id):
    url = f"http://192.168.0.105:8090/countries/{id}"
    response = requests.delete(url)
    print(response)
    
get()
insert()
get_country_by_id(3)
update(4)
delete(2)