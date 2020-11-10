# 10/28
# def __repr__(self):
#     return(f"The employee {self.first} {self.last} earns {self.pay}.")
# def __add__(self,other):
#     return self.pay + other.pay

class Employee:
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
    def __repr__(self):
      return(f"The employee {self.first} {self.last} earns {self.pay}.")
    def __add__(self, other):
      return self.pay + other.pay
emp1 = Employee('John', 'Williams', 90000)
emp2 = Employee('Alex', 'D', 50000)
print(emp2+emp1)
print(emp2)

# 1. setting 
# creat new repo , push code to repo, go to setting, manager acccess, invite collaborator
# code, Code, HTTPS,  
# One member of the team creates a folder on their local machine with the initial code. Remember to add a gitignore file if you are coming from Mac.
# This person then goes to Github and creates a new repository.
# After creating the repository and pushing code there, go to settings:
# https://share.squarespace.com/8LurYz2Q
# Click Manage Access > Invite Collaborator:
# https://share.squarespace.com/L1uQvZn6
# ================================
# The Collaborators:
# Need to check their email to accept the invitation
# Need to go to the repository online
# Click Code > Clone with HTTPS
# https://share.squarespace.com/NQu1pGkY
# Open up the terminal, CD into your workspace, and clone the repository using the terminal

