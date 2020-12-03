"""

"""

import requests

API_KEY = "8af2aa7fa978da0c3dc608a85406875c"
API_URL = "http://api.openweathermap.org/data/2.5/weather"
def getApi(loc):
    ret = requests.get(f"{API_URL}?q={loc}&appid={API_KEY}")
    return ret.json()

def main():
    try:
        loc = input("what city ")
        ret = getApi(loc)
        weather = ret["weather"][0]["description"]
        temp = format(float(ret["main"]["temp"]) - 273.1, '.2f')
        print(f"Its {temp} degrees in {loc} and {weather}")
    except Exception:
        print("error")
    

main()