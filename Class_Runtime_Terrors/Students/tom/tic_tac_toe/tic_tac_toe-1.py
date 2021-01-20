class Player :
    def __init__(self, name , token):
        self.name = name
        self.token = token
    def display (self):
        s ="It Your Turn " + str(self.name)
        return s
# class Game(Player):
#     def __init__(self, name, token, board):
#         super().__init__(length, width)
#         self.board = board


def get_selection():
    x = input (f'Select column 1, 2, or 3: ')
    while True:
        try:
            x = int(x)
            if x < 1 or x > 3:
                raise ValueError
            break
        except:
            print (f'"{x}" is an invalid column entry!')
            x = input (f'Select again column 1, 2, or 3: ')

    y = input (f'Select row 1, 2, or 3: ')
    while True:
        try:
            y = int(y)
            if y < 1 or y > 3:
                raise ValueError
            break
        except:
            print (f'"{y}" is an invalid row entry!')
            y = input (f'Select again row 1, 2, or 3: ')
    return x, y


def move(x, y): # does "player" need to be one of the variables as shown in the example?
    if x == 1 and y == 1:
        position = 0
    elif x == 2 and y == 1:
        position = 1
    elif x == 3 and y == 1:
        position = 2
    elif x == 1 and y == 2:
        position = 3
    elif x == 2 and y == 2:
        position = 4
    elif x == 3 and y == 2:
        position = 5
    elif x == 1 and y == 3:
        position = 6
    elif x == 2 and y == 3:
        position = 7
    elif x == 3 and y == 3:
        position = 8
    return position

def board():
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(gameboard[0], gameboard[1], gameboard[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(gameboard[3], gameboard[4], gameboard[5]))
    print('\t_____|_____|_____')
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(gameboard[6], gameboard[7], gameboard[8]))
    print("\t     |     |")
    print("\n")

def winning (gameboard):
    if gameboard[0]==  'X' and gameboard[1] == 'X' and gameboard[2] == 'X':
        print('X wins')
        return True
    elif gameboard[3]==  'X' and gameboard[4] == 'X' and gameboard[5] == 'X':
        print('X wins')
        return True
    elif gameboard[6]==  'X' and gameboard[7] == 'X' and gameboard[8] == 'X':
        print('X wins')
        return True
    elif gameboard[0]==  'X' and gameboard[3] == 'X' and gameboard[6] == 'X':
        print('X wins')
        return True
    elif gameboard[1]==  'X' and gameboard[4] == 'X' and gameboard[7] == 'X':
        print('X wins')
        return True
    elif gameboard[2]==  'X' and gameboard[5] == 'X' and gameboard[8] == 'X':
        print('X wins')
        return True
    elif gameboard[0]==  'X' and gameboard[4] == 'X' and gameboard[8] == 'X':
        print('X wins')
        return True
    elif gameboard[2]==  'X' and gameboard[4] == 'X' and gameboard[6] == 'X':
        print('X wins')
        return True
    if gameboard[0]==  'O' and gameboard[1] == 'O' and gameboard[2] == 'O':
        print('o wins')
        return True
    elif gameboard[3]==  'O' and gameboard[4] == 'O' and gameboard[5] == 'O':
        print('O wins')
        return True
    elif gameboard[6]==  'O' and gameboard[7] == 'O' and gameboard[8] == 'O':
        print('o wins')
        return True
    elif gameboard[0]==  'O' and gameboard[3] == 'O' and gameboard[6] == 'O':
        print('o wins')
        return True
    elif gameboard[1]==  'O' and gameboard[4] == 'O' and gameboard[7] == 'O':
        print('o wins')
        return True
    elif gameboard[2]==  'O' and gameboard[5] == 'O' and gameboard[8] == 'O':
        print('o wins')
        return True
    elif gameboard[0]==  'O' and gameboard[4] == 'O' and gameboard[8] == 'O':
        print('o wins')
        return True
    elif gameboard[2]==  'O' and gameboard[4] == 'O' and gameboard[6] == 'O':
        print('o wins')
        return True
    else:
        return False
   

def XO():
    while True:
     xo = input(f'Do you want to be X or O: ')
     xo.capitalize()
     if  xo == 'X' or xo == 'O':   
          return xo
     else:
          print('\nInvaid input X or O!')



player1n = input('What is your name Player 1: ')
player1t = XO()
player2n = input('What is your name Player 2: ') 

if player1t == 'X':
    player2t = 'O'
else:
    player2t = 'X'

gameboard = [' ' for x in range(9)] # Clear Board

player1= Player(player1n, player1t)
player2= Player(player2n, player2t)

turn = 1
while turn != 10:
    if (turn % 2) != 0:
        print(player1.display())
        box_selection = get_selection() # calls function to get player selection and returns x, y in tuple
        position = move(box_selection[0], box_selection[1]) # returns box number when given player x, y choice
    
        while gameboard[position] == 'X' or gameboard[position] == 'O':
            print ('That position is already taken. Choose again.')
            box_selection = get_selection()
            position = move(box_selection[0], box_selection[1])
        gameboard[position] = player1.token
        board()
        wincheck =  winning(gameboard)
        if wincheck == True:
            print(player1.name, ' You Won')
            break
        turn +=1
    
    else:
        print(player2.display())
        box_selection = get_selection() # calls function to get player selection and returns x, y in tuple
        position = move(box_selection[0], box_selection[1]) # returns box number when given player x, y choice    

        while gameboard[position] == 'X' or gameboard[position] == 'O':
            print('That position is already taken. Choose again.')
            box_selection = get_selection()
            position = move(box_selection[0], box_selection[1])
        gameboard[position] = player2.token
        board()
        wincheck =  winning(gameboard)
        if wincheck == True:
            print(player2.name, ' You Won')
            break
        turn +=1
if turn == 10:
    print('Draw')