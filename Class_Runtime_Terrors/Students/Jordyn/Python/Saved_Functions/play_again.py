def play_again():
    yes_list = ["yes", "ya", "y"]
    no_list = ["no", "nah", "n"]
    while True:
        replay = input("Would you like to make more change? Y/N\n> ").lower()
        if replay in yes_list:
            return True
        elif replay in no_list:
            return False
        else:
            print("Sorry, that was not a supported option.")