#VERSION 1

#making change by breaking total (jar) into units of 
# 100, 50, 25, 10, 5, and 1. Print result

#prompt input
jar = float(input('''How much, in dollars and cents ?.??, do you 
have to convert? '''))

jar = int(jar * 100)

Sacajawea = jar // 100 
remainder = jar % 100

half_dollars = remainder // 50
remainder = remainder % 50

quarters = remainder // 25
remainder = remainder % 25

dimes = remainder // 10
remainder = remainder % 10

nickels = remainder // 5
remainder = remainder % 5

pennys = remainder

print(f'''Your change is; 
{Sacajawea} Sacagawea dollars, 
{half_dollars} half dollars, 
{quarters} quarters, 
{dimes} dimes, 
{nickels} nickels,
and {pennys} pennys''')