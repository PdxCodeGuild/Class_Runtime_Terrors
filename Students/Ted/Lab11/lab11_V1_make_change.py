#VERSION 1

#making change by breaking total (jar) into units of 
# 100, 50, 25, 10, 5, and 1. Print result

#prompt input
jar = int(input('''How much, in 1 cent increments, do you 
have to convert? '''))

s = jar // 100
sd = s * 100
h = (jar - sd)//50
hd = h * 50
q = (jar - sd - hd)//25
qd = q * 25
d = (jar - sd - hd - qd)//10
dd = d * 10
p = (jar - sd - hd - qd - dd)

print(f'''Your change is; 
{s} Sacagawea dollars, 
{h} half dollars, 
{q} quarters, 
{d} dimes, 
and {p} pennys''')