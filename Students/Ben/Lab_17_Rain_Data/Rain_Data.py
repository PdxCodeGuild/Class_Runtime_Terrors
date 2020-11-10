import requests

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
print(response.text)