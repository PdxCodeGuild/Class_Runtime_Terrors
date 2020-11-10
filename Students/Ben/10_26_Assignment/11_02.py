nums = [x**2 for x in range(10)]

print(nums)

numb = []
for x in range (10):
    nums.append(x**2)
print(nums)

# names = ["David", 'Alex', "Tom"
# lower = [name.lower()]]

years = [1995 ,200, 2004, 2011]
leap_years = [year for year in years if year % 4 == 0]
print(leap_years)

numbers = [1,2,3,4,5]
double_odds = []
for x in numbers:
    if x % 2 == 1:
        double_odds.append(x)
print(double_odds)

double_odds = [n*2 for n in numbers if n % 2 == 1]

print({x // 10 for x in range(100)})

names_to_ages = {'Amanda': '90',"David": "50"}
print({name: int(age)for name, age in names_to_ages.items()})