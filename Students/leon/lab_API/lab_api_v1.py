'''PDX Fullstack lab API with Brad version 1
will get user input on what info they want from the API 
and then display it '''

 
import requests

def main():
    endgame = False
    apikey = "8af2aa7fa978da0c3dc608a85406875c"

    while not endgame:
        
        choice = input("Enter a city name: ").lower()

        weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={choice}&appid={apikey}")

        cast = weather.json()

        print(cast)

        end = input("Check another city? y/n ")
        if end == 'n':
            endgame = True
        else: 
            continue

    print("Happy trails.")

main()

