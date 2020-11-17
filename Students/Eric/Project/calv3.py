import math
from tkinter import *

root = Tk() #Creating Root Tkinter Widget
root.title("Calculator") #GUI Tittle 

cell = Entry(root,width =17, borderwidth=10, font=("Courier", 32)) 
cell.grid(row=0, column=0, columnspan=5, padx=10,pady=10)

def button_click(number): # Input onto Display Fuction
	current = cell.get()
	cell.delete(0, END)
	cell.insert(0, str(current) + str(number))

def button_click_dot(number): # Input onto Display Fuction
	current = cell.get()
	if current.find('.')==-1: # If . is not found
		cell.delete(0, END)
		cell.insert(0, str(current) + str(number))

def button_clear(): # Clear Display
	cell.delete(0, END)

def float_check(first_number): # Check for Float
	global f_num
	global operation 
	try:
		f_num =float(first_number)
		cell.delete(0, END)
	except:
		cell.delete(0, END)
		cell.insert(0,"Error")

def button_add(): # + Fuction
	first_number = cell.get()
	global f_num
	global operation 
	operation = "+"
	float_check(first_number)

def button_sub():# - Fuction
	first_number = cell.get()
	global f_num
	global operation 
	operation = "-"
	float_check(first_number)

def button_time(): # * Fuction
	first_number = cell.get()
	global f_num
	global operation 
	operation = "*"
	float_check(first_number)

def button_div(): # / Fuction
	first_number = cell.get()
	global f_num
	global operation 
	operation = "/"
	float_check(first_number)

def button_abs(): # +/- Fuction
	first_number = cell.get()
	try:
		first =float(first_number)*-1
		cell.delete(0, END)
		cell.insert(0, first)
	except:
		cell.delete(0, END)
		cell.insert(0,"Error")

def button_x2(): # + X^2 Fuction
	first_number = cell.get()
	try:
		first =float(first_number)*float(first_number)
		first = round(first, 6)
		cell.delete(0, END)
		cell.insert(0, first)
	except:
		cell.delete(0, END)
		cell.insert(0,"Error")

def button_sr(): # Square Root Fuction
	first_number = cell.get()
	try:
		if float(first_number) == 0.0: # Check For Zero
			cell.delete(0, END)
			cell.insert(0,"Error")
		else:
			first =math.sqrt(float(first_number))
			first = round(first, 6)
			cell.delete(0, END)
			cell.insert(0, first)
	except:
		cell.delete(0, END)
		cell.insert(0,"Error")

def button_inv(): # 1/x Fuction
	first_number = cell.get()
	try:
		if float(first_number) == 0.0: # Zero Check
			cell.delete(0, END)
			cell.insert(0,"Error")
		else:
			first =1/float(first_number)
			cell.delete(0, END)
			cell.insert(0, first)
	except:
		cell.delete(0, END)
		cell.insert(0,"Error")

def button_del(): # Backspace
	first_number = cell.get()
	try:
		first = first_number[:-1]
		cell.delete(0, END)
		cell.insert(0, first)
	except:
		cell.delete(0, END)
		cell.insert(0,"Error")

def button_exp(): # E^ Fuction
	first_number = cell.get()
	try:
		first = math.exp(float(first_number))
		cell.delete(0, END)
		cell.insert(0, first)
	except:
		cell.delete(0, END)
		cell.insert(0,"Error")

def button_pc(): # % Fuction
	first_number = cell.get()
	try:
		first = (float(first_number))/100
		cell.delete(0, END)
		cell.insert(0, first)
	except:
		cell.delete(0, END)
		cell.insert(0,"Error")

def button_equal(): # = Fuction
	second_number = cell.get()
	try: 
		cell.delete(0, END)
		if operation == "+":
			cell.insert(0, f_num + float(second_number))
		if operation == "-":
			cell.insert(0, f_num - float(second_number))
		if operation == "*":
			cell.insert(0, f_num * float(second_number))
		if operation  == "/" and float(second_number) == 0.0:
			cell.delete(0, END)
			cell.insert(0,"Error")
		if operation == "/":
			cell.insert(0, f_num / float(second_number))
	except:
		cell.delete(0, END)
		cell.insert(0,"Error")
	
# Define Buttons
button_1 = Button(root, text ="1",padx=40.5, pady=20, font=("Courier", 18),command=lambda: button_click(1)) # 1
button_2 = Button(root, text ="2",padx=40.5, pady=20, font=("Courier", 18), command=lambda: button_click(2)) # 2
button_3 = Button(root, text ="3",padx=40, pady=20, font=("Courier", 18), command =lambda: button_click(3)) # 3
button_4 = Button(root, text ="4",padx=40.5, pady=20, font=("Courier", 18), command=lambda: button_click(4)) # 4
button_5 = Button(root, text ="5",padx=40.5, pady=20, font=("Courier", 18), command=lambda: button_click(5)) # 5
button_6 = Button(root, text ="6",padx=40, pady=20, font=("Courier", 18), command=lambda: button_click(6)) # 6
button_7 = Button(root, text ="7",padx=40.5, pady=20, font=("Courier", 18), command=lambda: button_click(7)) # 7
button_8 = Button(root, text ="8",padx=40.5, pady=20, font=("Courier", 18), command=lambda: button_click(8)) # 8
button_9 = Button(root, text ="9",padx=40, pady=20, font=("Courier", 18), command=lambda: button_click(9)) # 9
button_0 = Button(root, text ="0",padx=40.5, pady=20, font=("Courier", 18), command=lambda: button_click(0)) # 0
button_equal = Button(root, text ="=",padx=39, pady=20,font=("Courier", 18), command=button_equal) # Equal
button_clear = Button(root, text ="C",padx=39.5, pady=20, font=("Courier", 18), command=button_clear) # Clear
button_add = Button(root, text ="+",padx=39, pady=20, font=("Courier", 18), command=button_add) # Add
button_sub = Button(root, text ="-",padx=39, pady=20, font=("Courier", 18), command=button_sub) # Sub
button_time = Button(root, text ="*",padx=39, pady=20, font=("Courier", 18), command=button_time) # Mutli
button_div = Button(root, text =chr(247),padx=39, pady=20, font=("Courier", 18), command=button_div) # Div
button_dot= Button(root, text =".",padx=39.5, pady=20, font=("Courier", 18), command=lambda: button_click_dot(".")) # Dot
button_abs = Button(root, text ="+/-",padx=27, pady=20, font=("Courier", 18), command=button_abs) # +/-
button_x2 = Button(root, text ="x^2",padx=27, pady=20, font=("Courier", 18), command=button_x2) # X^2
button_sr = Button(root, text =chr(8730),padx=39.5, pady=20, font=("Courier", 18), command=button_sr) #Square Root
button_inv = Button(root, text ="1/x",padx=26.5, pady=20, font=("Courier", 18), command=button_inv) # 1/X
button_del = Button(root, text =chr(171),padx=39, pady=20, font=("Courier", 18), command=button_del) # Backspace
button_exp = Button(root, text ="e^x",padx=27, pady=20, font=("Courier", 18), command=button_exp) # Exp
button_pc = Button(root, text ="%",padx=40.5, pady=20, font=("Courier", 18), command=button_pc) # %

# Buttons on Cal
button_pc.grid(row=1, column=0)
button_exp.grid(row=1, column=1)
button_clear.grid(row=1, column=2)
button_del.grid(row=1, column=3 )

button_inv.grid(row=2, column=0)
button_x2.grid(row=2, column=1)
button_sr.grid(row=2, column=2)
button_div.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_time.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_sub.grid(row=4, column=3)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_add.grid(row=5, column=3)

button_abs.grid(row=6, column=0 )
button_0.grid(row=6, column=1 )
button_dot.grid(row=6, column=2)
button_equal.grid(row=6, column=3)

root.mainloop()