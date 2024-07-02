import requests

# GET: Adatokat kérhetünk le
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    print(response.content)
else:
    print(f"Hiba történt: {response.status_code}")

# POST: Adatok küldése
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post(url, json=data)
if response.status_code == 201:
    print(response.content)
else:
    print(f"Error occured: {response.status_code}")

# PUT: Adatok módosítása/frissítése
url = "https://jsonplaceholder.typicode.com/posts/1"
data = {"title": "updated title", "body": "updated body", "userId": 1}
response = requests.put(url, json=data)
if response.status_code == 200:
    print(response.content)
else:
    print(f"Error occured: {response.status_code}")

# DELETE: Adatok törlése
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)
if response.status_code == 200:
    print("Deleted successfully!")
else:
    print(f"Error occured: {response.status_code}")
