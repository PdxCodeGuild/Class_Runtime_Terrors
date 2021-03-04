from tkinter import *
from tkinter import messagebox
import requests

root = Tk()
root.title("Calculator")

v1 = IntVar()
v1.set("2")

def click(value):
   lab = Label(root, text=v1.get())
#    lab.pack() 

Radiobutton(root, text ="Option 1" , variable=v1, value =1,command=lambda: click(v1.get())).pack()
Radiobutton(root, text ="Option 2" , variable=v1, value =2,command=lambda: click(v1.get())).pack()

but = Button(root,text ="Run",command=lambda: click(v1.get()))
but.pack()
mainloop()