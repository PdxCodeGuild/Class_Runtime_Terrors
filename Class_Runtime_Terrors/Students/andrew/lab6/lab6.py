'''Lab 6 Password Generator'''
import random
import string

chars = string.ascii_letters + string.digits 

n = random.randint(8, 16)


def pass_gen():
	print('Welcome to Andrews Password Generator \n')
	print('This program creates passwords out of thin air! \n')
	password = ""
	i = 0
	while i < n:
		password += random.choice(chars)
		i = i + 1
	
	print(f'Your password is {password}')



def pass_gen_v2():
	print('Welcome to Andrews Password Generator version 2.0! \n')
	print('This program creates passwords from a number YOU enter! \n')
	while True:
		num = input("Enter a number from 4 to 18: \n")
		if int(num) >= 4 and int(num) <= 18:
			password = ""
			i = 0
			while i < int(num):
				password += random.choice(chars)
				i = i + 1
			print(f'Your password is {password} \n')
			print("Version 3 comming soon!")
			break
		else:
			print('\nInvaid input try again!')

def main():
	pass_gen()
	pass_gen_v2()

main()



