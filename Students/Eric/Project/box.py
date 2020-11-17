from tkinter import *
from tkinter import messagebox
import requests


def apirecall():
    url = 'https://api.covid19api.com/summary'
    summary = requests.get(url)
    return summary.json()


def popup():
	messagebox.showinfo("This is my Popup!", "Hello World!")


root = Tk()
root.title("Covid 19 Tracker")

e = Entry(root,width =50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

Button(root, text="Popup", command=popup).grid(row=1, column=1, columnspan=3, padx=10,pady=10)


mainloop()

'''
import requests

def main():
    print('\nPick from the following opitions:\n')
    print('\t1.) Current Global Covid 19 Numbers')
    print('\t2.) Covid 19 Numbers by Country')
    print('\t3.) Exit Tracker Program')
    input = inputpick()
    if input == 1:
        user1()
    elif input == 2:
        user2()
    else:
        print("\nStay Safe!\n")

def inputpick():
    while True:
        try:
            pick =int(input('\nWant do you want to do? :'))
            if pick == 1:
                return 1
            elif pick == 2:
                return 2
            elif pick == 3:
                return 3
            else:
                print('Invaild Input')
        except:
            print('Invaild Input Pick 1,2 or 3!')

def user1():
    data = apirecall()
    print('\nCOVID-19 Summary for Globally for the last 24 hours')
    print('New Confirmed Case: ',data['Global']['NewConfirmed'])
    print('New Deaths: ', data['Global']['NewDeaths'])
    print('New Recovered: ',data['Global']['NewRecovered'])
    print('Total Confirmed cases:',data['Global']['TotalConfirmed'])
    print('Total Deaths :',data['Global']['TotalDeaths'])
    print('Total Recovered: ',data['Global']['TotalRecovered'])
    main()

def user2():
    data = apirecall()
    recallx = 9000
    country = input('Enter your country : ')
    for x in range(len(data['Countries'])):
        if data['Countries'][x]['Country'] == country:
            recallx = x  
    if recallx != 9000:
        print('\nCOVID-19 Summary for',country,'as of ',data['Countries'][recallx]['Date'],' in the last 24 hours')
        print('New Confirmed Case: ',data['Countries'][recallx]['NewConfirmed'])
        print('New Deaths: ', data['Countries'][recallx]['NewDeaths'])
        print('New Recovered: ',data['Countries'][recallx]['NewRecovered'])
        print('Total Confirmed cases:',data['Countries'][recallx]['TotalConfirmed'])
        print('Total Deaths :',data['Countries'][recallx]['TotalDeaths'])
        print('Total Recovered: ',data['Countries'][recallx]['TotalRecovered'])
    else:
        print('Country Not Found, Check your spelling and Try again')
    main()

def apirecall():
    url = 'https://api.covid19api.com/summary'
    summary = requests.get(url)
    return summary.json()

print('\n\nWelcome Covid-19 Tracker\n')

main()
'''