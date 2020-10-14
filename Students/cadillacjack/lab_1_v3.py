# trying to figure out the conversion
# matrix here


convert = {
"ft": 0.3048,
"mi": 1609.34,
"m": 1.0,
"km": 1000.0,
"yard": 0.9144,
"inch": 0.0254}

def blah(start, end):
    starter = start * convert["m"]
    print(1)
    ender = end * convert["m"]
    print(2)
    print(starter / ender)


def main():
    first = input("Check one ; ")
    second = input("Check two ; ")

    first = convert[first]
    second = convert[second]

    print(blah(first, second))

main()




