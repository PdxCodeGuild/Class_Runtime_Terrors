#password_generator.py
import string
import random
my_password = input("Enter a number \n:")
out_string = ""
for i in range (0, int(my_password)):
    random_password = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    out_string = out_string + random_password
print(f"Your password is: {out_string}")

