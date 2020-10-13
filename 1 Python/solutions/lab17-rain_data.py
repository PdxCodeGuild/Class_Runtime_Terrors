


# def average(x):
#     total = 0
#     n = len(x)
#     for i in range(n):
#         total += x[i]
#     total *= 1/n
#     return total

# print(average([1,2,3,4,5]))



import requests
from datetime import datetime
import math
import re
import matplotlib.pyplot as plt

def load_data(url):


    data = []

    response = requests.get(url)
    lines = response.text.split('\n')
    lines = lines[11:]
    for line in lines:
        columns = line.split()
        if len(columns) < 2:
            continue
        # print(columns[0], columns[1])
        
        date = columns[0]
        daily_total = columns[1]

        if daily_total == '-':
            continue

        date = datetime.strptime(date, '%d-%b-%Y')
        daily_total = float(daily_total)*0.01*2.54

        data.append((date, daily_total))
    
    return data

def load_data_regex(url):
    response = requests.get(url) 
    data = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)', response.text)
    for i in range(len(data)):
        date = data[i][0]
        daily_total = data[i][1]
        date = datetime.strptime(date, '%d-%b-%Y')
        daily_total = float(daily_total)*0.01*2.54
        data[i] = (date, daily_total)
    return data


def calculate_average(data):
    total = 0
    for row in data:
        total += row[1]
    return total / len(data)

def calculate_variance(data, mean):
    total = 0
    for row in data:
        total += (row[1] - mean) ** 2
    return total / len(data)


def rainiest_day(data):
    most_rain = None
    for row in data:
        if most_rain is None or row[1] > most_rain[1]:
            most_rain = row
    return most_rain


def chart_all(data):
    x_values = [row[0] for row in data]
    y_values = [row[1] for row in data]
    plt.plot(x_values, y_values)
    plt.show()

def chart_yearly_averages(data):
    monthly_totals = [0]*12 # [0,0,0,0,0,0,0,0,0,0,0,0]
    monthly_counts = [0]*12
    # month_names = [datetime(year=1, month=i+1, day=1).strftime('%B') for i in range(12)]
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print(month_names)
    for row in data:
        month = row[0].month-1
        monthly_totals[month] += row[1]
        monthly_counts[month] += 1
    monthly_averages = [monthly_totals[i]/monthly_counts[i] for i in range(12)]
    plt.plot(month_names, monthly_averages)
    plt.show()


# locations = {
#     'Hayden Island': 'https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain'
# }
data = load_data_regex('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
print(f'Loaded {len(data)} records')
mean = calculate_average(data)
print(f'The mean is {round(mean, 4)} cm')
variance = calculate_variance(data, mean)
standard_deviation = math.sqrt(variance)
print(f'The variance is {variance} cm^2')
print(f'The standard deviation is {standard_deviation} cm')
print(f'Meaning that 68.2% of the data will fall within {mean-standard_deviation} cm and {mean+standard_deviation} cm')

most_rain = rainiest_day(data)
most_rain_date = most_rain[0].strftime('%B %d, %Y')
print(f'The rainiest day was {most_rain_date} with {most_rain[1]} cm')

# chart_all(data)
chart_yearly_averages(data)

