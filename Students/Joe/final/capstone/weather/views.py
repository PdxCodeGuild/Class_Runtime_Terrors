from django.shortcuts import render
import requests
from .models import City 

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=8af2aa7fa978da0c3dc608a85406875c'
    # city = 'kaneohe'
    cities = City.objects.all()
    # print(cities)
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        # print(r)
        city_weather = {
            # 'city': city.name,
            'windspeed': r['wind']['speed'],
            'winddirection': r['wind']['deg'],
        }
        print(city_weather)
        weather_data.append(city_weather)
        # print(weather_data)


    context = {'weather_data': weather_data}
    print(context)
    return render (request, 'info/hawaiiinfo.html', context)

    
