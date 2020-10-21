'''PDX Fullstack lab API with Brad version 1
will get user input on what info they want from the API 
and then display it '''

 
import requests

def main():
    endgame = False
    apikey = "8af2aa7fa978da0c3dc608a85406875c"
    bull = False
    while not endgame:
        while not bull:      
            choice = input("Do you want to know current weather or a 5 day forecast? 'w' or 'f' ").lower()
            if choice == 'w':
                choice = 'weather'
                bull = True
            elif choice == 'f':
                choice = 'forecast'
                bull = True
            else:
                print("I don't understand.")
        
        city = input("Enter a city name: ").lower()

        weather = requests.get(f"https://api.openweathermap.org/data/2.5/{choice}?q={city}&units=imperial&appid={apikey}")

        cast = weather.json()
        
        i = 0
        if choice == 'weather':
            print(round(cast['main']['temp']))
        else: 
            while (i < 5):
                print(f"Day {i+1}: ", round(cast['list'][i]['main']['temp']))
                i += 1
                

        end = input("Check another city? y/n ")
        if end == 'n':
            endgame = True
        else: 
            continue

    print("Happy trails.")

main()

