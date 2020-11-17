import requests
response = requests.get(f"https://jsonplaceholder.typicode.com/todos/1")
data = response.json()
print(data)

pip3 install requests