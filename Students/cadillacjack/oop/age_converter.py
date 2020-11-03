from datetime import datetime

class How_old:
    def __init__(self, month, day, year):
        self.month = int(month)
        self.day = int(day)
        self.year = int(year)
    def convert(self):
        bday = datetime(self.year, self.month, self.day)
        date = datetime.now()
        alive = date - bday
        age = date.year - bday.year
        print(f'''
Your Birthday is : {bday}
You are {age} years old.
You have been alive (more or less): {alive})''')
        

initiate = input('''
This program will display how many seconds
since Midnight on your Birthday have elapsed.

Would you like to know (approximately) how many seconds you have been alive?
Enter a "y" for Yes, or an "n" to Exit
- ''')

if initiate == "y":
    month = input('''
Enter the Month you were born as a number between 1 and 12 : ''')
    day = input(''' 
Enter the Day you were born as a number between 1 and 31 : ''')
    year = input('''
Enter the Year you were born as a 4 digit Year. ex: 1987
Year : ''')

a = How_old(month, day, year)
How_old.convert(a)