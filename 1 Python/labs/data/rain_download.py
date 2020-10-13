import datetime
import re
import requests
import matplotlib.pyplot as plt

# r = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
# contents = r.text



url = 'https://or.water.usgs.gov/non-usgs/bes/'
def get_locations():
    r = requests.get(url)
    locations = re.findall(r'(\w+)\.rain', r.text)
    locations.sort()
    return locations

def get_file(location):
    r = requests.get(url + location + '.rain')
    return r.text


def parse_date(date_str):
    date = datetime.datetime.strptime(date_str, '%d-%b-%Y')
    return (date.year, date.month, date.day)


# locations = get_locations()
# print('\n'.join([f'{i} {location}' for i, location in enumerate(locations)]))
# i = int(input('enter a number: '))
# print(get_file(locations[i]))


locations = get_locations()
print(locations)
print(len(locations))

d = {}
for i in range(len(locations)):
    contents = get_file(locations[i])

    data = re.findall('(\d{2}-\w{3}-\d{4}) +(\d+)', contents)
    data = [(parse_date(data[i][0]), int(data[i][1])*0.01*2.54) for i in range(len(data))]
    for row in data:
        if row[0] in d:
            d[row[0]][i] = row[1]
        else:
            d[row[0]] = [None] * len(locations)


    print(f'{round(i/len(locations)*100,2)}%')

# print('\n'.join([f'{date}\t{d[date]}' for date in d]))

d = list(d.items())
d.sort(key=lambda t: t[0][2])
d.sort(key=lambda t: t[0][1])
d.sort(key=lambda t: t[0][0])

# print('\n'.join([f'{r[0][0]} {r[0][1]} {r[0][2]}' for r in d]))



output = 'date,' + ','.join(locations) + '\n'
for r in d:
    date = f'{r[0][0]} {r[0][1]} {r[0][2]}'
    values = [str(v) if v is not None else '' for v in r[1]]
    output += date + ',' + ','.join(values) + '\n'

with open('rain_output.csv', 'w') as f:
    f.write(output)




