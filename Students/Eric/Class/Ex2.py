# Exercise number 2)
# a) Import datetime
# b) Create a class with the following attributes:
# name
# last name
# surname
# address
# age
# telephone
# email
# Create a method that based on today’s time can return the person’s age. For instance, if this person was born in (1992, 3, 12) and I use this method, I should get 28 as a result

# from datetime import date 
  
# def Age(birthDate): 
#     today = date.today() 
#     age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  
#     return age 
      
# # Driver code  
# # print(Age(date(1997, 2, 3)), "years") 
import datetime 
from datetime import date 



age = datetime.date.today() - date(1997, 2, 3)
print(age)
