class Player :
    def __init__(self, name , token):
        self.name = name
        self.token = token
class Game(Player):
    def __init__(self, name, token, board):
        super().__init__(length, width)
        self.board = board


player1n = input('What is your name Player 1: ')
player1t = input('Do you wnat to use the X or O: ')
player2n = input('What is your name Player 1: ') 

if player1t == 'X':
    player2t = 'O'
else:
    player2t == 'X'

player1= Player(player1n, player1t)
player2= Player(player2n, player2t)
values = [' ' for x in range(9)]
print("\n")
print("\t     |     |")
print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
print('\t_____|_____|_____')
print("\t     |     |")
print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
print('\t_____|_____|_____')
print("\t     |     |") 
print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
print("\t     |     |")
print("\n")