#!/bin/python3
# Filename: tictactoe.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Leon || Cleon || Peter, Students
# Assignment: Tic-Tac-Toe - Version 1
# Date: 10/28/2020
# Version 36.0.47b



# PDX Fullstack: Tic Tac Toe 
# You will write a **Player** class and **Game** class to model Tic Tac Toe, and a function **main** that models gameplay taking in user inputs through REPL.

# The Player class has the following properties: 
#* **name** = *player name*
#* **token** = *'X' or 'O'*
# Peter Entries Starts:
class Player:
    def __init__(self, name, token): 
        self.name = name
        self.token = token

# Peter Entries Ends:

# The Game class has the following properties:
# * **board** = *your representation of the board* <Cleon>
# You can represent the board however you like, such as a 2D list, tuples, or dictionary.
# The Game class has the following methods:
# <Leon> * `__repr__()` Returns a pretty string representation of the game board
# * 'move(x, y, player)' place a player's token character at a given coordinate 
# * 'calc_winner()' determines if a victory condition is met by a Player
# * 'is_full()' returns True if the game board is full and no victory condition met
# * 'is_game_over()' returns True if game board is full or a player has won

class Game:
    def __init__(self):

        self.board = {'1': ' ',
                        '2': ' ',
                        '3': ' ',
                        '4': ' ',
                        '5': ' ',
                        '6': ' ',
                        '7': ' ',
                        '8': ' ',
                        '9': ' '}
    def __repr__(self):
        # pretty print board
        return f"{self.board['1']}|{self.board['2']}|{self.board['3']}\n-+-+-\n{self.board['4']}|{self.board['5']}|{self.board['6']}\n-+-+-\n{self.board['7']}|{self.board['8']}|{self.board['9']}\n"
        
    def move(self, turn, player):
        # place tokens over the board
        if turn in self.board:
            self.board[turn] = player.token
            

    def calc_winner(self, p1, p2):
        # check if winning condition met
        vic = '' # fill with either p1 or p2
        players = [p1, p2]
        for player in players:
        # horizontal_win_conditions = iterate 3 rows

            if player.token == self.board['1'] == self.board['2'] == self.board['3']:
                vic = player
            if player.token == self.board['4'] == self.board['5'] == self.board['6']:
                vic = player
            if player.token == self.board['7'] == self.board['8'] == self.board['9']:
                vic = player
        # vertical win condition = iterate 3 columns
            if player.token == self.board['1'] == self.board['4'] == self.board['7']:
                vic = player
            if player.token == self.board['2'] == self.board['5'] == self.board['8']:
                vic = player
            if player.token == self.board['3'] == self.board['6'] == self.board['9']:
                vic = player
        # l-diagonal
            if player.token == self.board['1'] == self.board['5'] == self.board['9']:
                vic = player
        # r-diagonal
            if player.token == self.board['3'] == self.board['5'] == self.board['7']:
                vic = player
        return vic

    def is_full(self):
        # check if draw condition met
        fullORnah = all(value == "X" or value == "O"  for value in self.board.values()) # Checks if all the values in dictionary are "X" or "O". Returns True or False
        return fullORnah

    def is_game_over(self, p1, p2):
        # check if either calc_wnner OR is_full are True
        vic = self.calc_winner(p1, p2)
        draw = self.is_full()
        if draw == True:
            return True
        elif vic != '':
            return True
        else:
            return False

def main():
    game_on = Game()
    print("\tTic Tac Toe")
    print(repr(game_on))
    player1 = input("Enter name for P1 (X): ")
    player2 = input("Enter name for P2 (O): ")
    p1 = Player(player1, 'X')
    p2 = Player(player2, 'O')
    plist = [p1, p2]
    print("\tValid moves are, from top-left going across:")
    print("\t1, 2, 3; 4, 5, 6; 7, 8, 9")
    endgame  = False
    # add a loop layer to make replayable...
    while not endgame: 
        for player in plist:
            while True:
                try:
                    turn = input(f"Enter a square to take, {player.name}: ")
                    print("\n")
                    if ((turn in game_on.board) & (game_on.board[turn] == ' ')):
                        game_on.move(turn, player)
                        break
                    else: 
                        print("Try again.")
                except KeyError:
                    print("Try again.")

            print(repr(game_on))

            vic = game_on.calc_winner(p1, p2)

            end = game_on.is_game_over(p1, p2)

            if end == True:
                endgame = True
                break
    if vic == '':
        print("Draw")
    else:
        print(f"{vic.name} wins.")


main()



