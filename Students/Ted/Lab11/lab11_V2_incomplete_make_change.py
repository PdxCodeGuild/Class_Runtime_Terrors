#VERSION 1

#making change by breaking total (jar) into units of 
# 100, 50, 25, 10, 5, and 1. Print result

#prompt input
jar = float(input('''How much, in dollars and cents ?.??, do you 
have to convert? '''))

jar = int(jar * 100)

Sacajawea = jar // 100 
remainder = jar %
half_dollars = jar % 100 // 50

quarters = jar % 50 // 25

dimes = jar % 25 // 10

nickels = jar % 10 // 5

pennys = jar % 5 // 1

print(f'''Your change is; 
{Sacajawea} Sacagawea dollars, 
{half_dollars} half dollars, 
{quarters} quarters, 
{dimes} dimes, 
{nickels} nickels,
and {pennys} pennys''')