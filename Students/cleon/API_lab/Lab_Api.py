#help("modules")
import requests

url = 'api.openweathermap.org/data/2.5/weather' 
key = ''
webiste = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={name}")


