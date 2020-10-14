#User Login

user_list = [ #List version with seperate dictionaries
    {
        'username':'Gandalf', 'password':'TheWhite'
    },
    {
        'username': 'bilboBaggins', 'password': 'theShire123'
    },
    {
        'username': 'iAmSmeagol', 'password': 'myPrecious!'
    }
]


def login(username,password):
    for user_profile in user_list:
        if username_attempt == user_profile['username']:
            if password_attempt == user_profile['password']:
                return True
            elif password_attempt != user_profile['password']:
                return False
                
        elif username_attempt != user_profile['username']:
            return False

        else:
            continue


print("Profile:")
repeat = 3

while repeat > 0:
    username_attempt = input("    username: ") #User input for username
    password_attempt = input("    password: ") #User input for password

    login_attempt = login(username_attempt,password_attempt) #runs login() function for True/False statement

    if repeat == 1: #Breaks the code if no username/password combo has succeeded
        print("Attempt Limit Reached! Please try again another time!")
        break
    elif login_attempt == True: #Allows the user in, currently just ends code
        repeat -= 3
        print(f"Welcome, {username_attempt}")
    elif login_attempt == False: #Alerts the user of a general error and number of remaining attempts allowed
        repeat -= 1
        print(f"Error! Your username or password was incorrect!\nAttempts Remaining: {repeat}")
    else:
        print("something has gone wrong") #This took me a long time and I needed help very badly...