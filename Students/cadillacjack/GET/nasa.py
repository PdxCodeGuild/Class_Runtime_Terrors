import requests

my_site = requests.get(f"https://api.nasa.gov/planetary/apod?api_key=4sGZ9oQpr4FqOaBewnmjODONv5FPIoOYB4dq6acz")

data = my_site.json()

print(data["hdurl"])