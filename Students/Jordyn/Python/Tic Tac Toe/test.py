import operator
import random

class Game:
    def __init__(self):
        self.breaker = 0
        while self.breaker != 1:
                try:
                    self.difficulty = int(input("Please choose your difficulty 1-10. 1 being easiest and 10 being impossible.\n> "))
                    if self.difficulty not in range(1, 11):
                        print("Invalid selection")
                    elif self.difficulty in range(1, 11):
                        self.breaker += 1
                except ValueError:
                    print("Please only use whole numbers")
        self.move = 0
        self.board_full = False
        self.game_over = False
        self.has_won = False
        self.valid_input = False
        self.game_board = {7: " ", 8: " ", 9: " ",
                           4: " ", 5: " ", 6: " ",
                           1: " ", 2: " ", 3: " "}

    def display_board(self):
        game_board = self.game_board
        print(game_board[7] + ' |' +
              game_board[8] + ' |' + game_board[9])
        print('--+--+--')
        print(game_board[4] + ' |' +
              game_board[5] + ' |' + game_board[6])
        print('--+--+--')
        print(game_board[1] + ' |' +
              game_board[2] + ' |' + game_board[3])

    def user_input(self, mark):
        user = 0
        while user != range(1, 10):
            try:
                user = int(input(f"Player {mark}, please choose a location on the board:\n> "))
                if user not in range(1, 10):
                    print("Invalid selection")
                elif self.is_occupied(user) == True:
                    print('Space already filled')
                elif user in range(1, 10):
                    return user
            except ValueError:
                print("Please only use whole numbers")
            except TypeError:
                print("Please use the numbers on your keyboard")
        return user 

    def is_board_full(self):
        # draw = ' '
        d = 0
        for x in range(1, 10):
            if self.game_board[x] != ' ':
                d += 1
        if d == 9:
            return True
        else:
            return False
  
    def is_occupied(self, choice):
        if self.game_board[choice] != " ":
            print("Block ocupied!")
            self.display_board()
            return True
        else:
            return False

    def is_valid_input(self, choice):
        choice = choice
        if not choice.isdigit():
            print("Invlaid input : NOT A DIGIT FROM 1-9")
        elif choice.isspace():
            print("Space not valid input")
        elif int(choice) < 1 or int(choice) > 9: # NOT IN RANGE(1,10)
            print("Invalid input : GREATER THAT 9 OR LESS THAN ONE")
        elif choice not in self.game_board:
            print("Not a valid square, 1 - 9 only")

        else:
            self.valid_input = True

    def check_win(self, char):
        '''Checks all possible win conditions'''
        for x in range(1, 10):
            # horizontal win
            y = self.y_func(x, 1)
            z = self.z_func(y, 1)

            if x == 1 or x == 4 or x == 7:
                if self.game_board[x] == char and self.game_board[y] == char and self.game_board[z] == char:
                    self.has_won = True
                    print(f'Player {char} has won! ')
            
        for x in range(1, 4):
            # vertical win
            y = self.y_func(x, 3)
            z = self.z_func(y, 3)

            if self.game_board[x] == char and self.game_board[y] == char and self.game_board[z] == char:
                self.has_won = True
                print(f'Player {char} has won! ')
            # diagonal check
        if self.game_board[7] == char and self.game_board[5] == char and self.game_board[3] == char:
            self.has_won = True
            print(f'Player {char} has won! ')
        
        if self.game_board[9] == char and self.game_board[5] == char and self.game_board[1] == char:
            self.has_won = True
            print(f'Player {char} has won! ')
        
        # self.has_won = False

    def y_func(self, x, var):
        '''Returns Y'''
        y = x + var
        if y > 9:
            y -= 9
        return y

    def z_func(self, y, var):
        '''Returns Z'''
        z = y + var
        if z > 9:
            z -= 9
        return z

class Player:
    def __init__(self):
        self.player_1 = ""
        self.player_2 = ""
        self.current_player = ""
        self.player_chosen = False
        while not self.player_chosen:
            self.current_player = input(
                "Please pick X or O to start the game: ").capitalize()
            print(self.current_player)
            if self.current_player == "X":
                self.player_1 = "X"
                self.player_2 = "O"
                self.player_chosen = True

            elif self.current_player == "O":
                self.player_1 = "O"
                self.player_2 = "X"
                self.player_chosen = True

    def player1(self):
        players = [self.player_1, self.player_2]
        return players

class Cpu:
    def __init__(self, game, player):
        self.weighted_board_defualt = {7: 0, 8: 0, 9: 0,
                                       4: 0, 5: 0, 6: 0,
                                       1: 0, 2: 0, 3: 0}
        self.weighted_board_win = {7: 0, 8: 0, 9: 0,
                                   4: 0, 5: 0, 6: 0,
                                   1: 0, 2: 0, 3: 0}
        self.weighted_board_block = {7: 0, 8: 0, 9: 0,
                                     4: 0, 5: 0, 6: 0,
                                     1: 0, 2: 0, 3: 0}
        self.game_board = game.game_board
        self.player = player
        self.difficulty = game.difficulty

    def weight_reset(self):
        self.weighted_board_win = self.weighted_board_defualt
        self.weighted_board_block = self.weighted_board_defualt

    def smart_choice_cpu(self):
        
        self.weighted_board_win = {7: 0, 8: 0, 9: 0,
                                   4: 0, 5: 0, 6: 0,
                                   1: 0, 2: 0, 3: 0}

        #if middle space is open, take it
        if self.game_board[5] == ' ':
            self.weighted_board_win[5] += 1

        #Horizontal weights
        #1-3
        if self.game_board[2] == self.player.player_2 and self.game_board[3] == self.player.player_2:
            if self.game_board[1] == ' ':
                self.weighted_board_win[1] += 1
        if self.game_board[1] == self.player.player_2 and self.game_board[2] == self.player.player_2:
            if self.game_board[3] == ' ':
                self.weighted_board_win[3] += 1
        if self.game_board[1] == self.player.player_2 and self.game_board[3] == self.player.player_2:
            if self.game_board[2] == ' ':
                self.weighted_board_win[2] += 1
        #4-6
        if self.game_board[4] == self.player.player_2 and self.game_board[5] == self.player.player_2:
            if self.game_board[6] == ' ':
                self.weighted_board_win[6] += 1
        if self.game_board[5] == self.player.player_2 and self.game_board[6] == self.player.player_2:
            if self.game_board[4] == ' ':
                self.weighted_board_win[4] += 1
        if self.game_board[4] == self.player.player_2 and self.game_board[6] == self.player.player_2:
            if self.game_board[5] == ' ':
                self.weighted_board_win[5] += 1
        #7-9
        if self.game_board[7] == self.player.player_2 and self.game_board[8] == self.player.player_2:
            if self.game_board[9] == ' ':
                self.weighted_board_win[9] += 1
        if self.game_board[8] == self.player.player_2 and self.game_board[9] == self.player.player_2:
            if self.game_board[7] == ' ':
                self.weighted_board_win[7] += 1
        if self.game_board[7] == self.player.player_2 and self.game_board[9] == self.player.player_2:
            if self.game_board[8] == ' ':
                self.weighted_board_win[8] += 1
        
        #Vertical weights
        #1,4,7
        if self.game_board[1] == self.player.player_2 and self.game_board[4] == self.player.player_2:
            if self.game_board[7] == ' ':
                self.weighted_board_win[7] += 1
        if self.game_board[4] == self.player.player_2 and self.game_board[7] == self.player.player_2:
            if self.game_board[1] == ' ':
                self.weighted_board_win[1] += 1
        if self.game_board[1] == self.player.player_2 and self.game_board[7] == self.player.player_2:
            if self.game_board[4] == ' ':
                self.weighted_board_win[4] += 1
        #2,5,8
        if self.game_board[2] == self.player.player_2 and self.game_board[5] == self.player.player_2:
            if self.game_board[8] == ' ':
                self.weighted_board_win[8] += 1
        if self.game_board[5] == self.player.player_2 and self.game_board[8] == self.player.player_2:
            if self.game_board[2] == ' ':
                self.weighted_board_win[2] += 1
        if self.game_board[2] == self.player.player_2 and self.game_board[8] == self.player.player_2:
            if self.game_board[5] == ' ':
                self.weighted_board_win[5] += 1
        #3,6,9
        if self.game_board[3] == self.player.player_2 and self.game_board[6] == self.player.player_2:
            if self.game_board[9] == ' ':
                self.weighted_board_win[9] += 1
        if self.game_board[6] == self.player.player_2 and self.game_board[9] == self.player.player_2:
            if self.game_board[3] == ' ':
                self.weighted_board_win[3] += 1
        if self.game_board[3] == self.player.player_2 and self.game_board[9] == self.player.player_2:
            if self.game_board[6] == ' ':
                self.weighted_board_win[6] += 1

        # #Diagonal weights
        if self.game_board[5] == self.player.player_2:
            if self.game_board[1] == self.player.player_2:
                if self.game_board[9] == ' ':
                    self.weighted_board_win[9] += 1
            if self.game_board[3] == self.player.player_2:
                if self.game_board[7] == ' ':
                    self.weighted_board_win[7] += 1
            if self.game_board[7] == self.player.player_2:
                if self.game_board[3] == ' ':
                    self.weighted_board_win[3] += 1
            if self.game_board[9] == self.player.player_2:
                if self.game_board[1] == ' ':
                    self.weighted_board_win[1] += 1

        # self.display_board_win()
        
    def smart_choice_player(self):

        self.weighted_board_block = {7: 0, 8: 0, 9: 0,
                                     4: 0, 5: 0, 6: 0,
                                     1: 0, 2: 0, 3: 0}

        # player_mark = self.player.player_1

        #Horizontal weights
        if self.game_board[2] == self.player.player_1 and self.game_board[3] == self.player.player_1:
            if self.game_board[1] == ' ':
                self.weighted_board_block[1] += 1
        if self.game_board[1] == self.player.player_1 and self.game_board[2] == self.player.player_1:
            if self.game_board[3] == ' ':
                self.weighted_board_block[3] += 1
        if self.game_board[1] == self.player.player_1 and self.game_board[3] == self.player.player_1:
            if self.game_board[2] == ' ':
                self.weighted_board_block[2] += 1

        if self.game_board[4] == self.player.player_1 and self.game_board[5] == self.player.player_1:
            if self.game_board[6] == ' ':
                self.weighted_board_block[6] += 1
        if self.game_board[5] == self.player.player_1 and self.game_board[6] == self.player.player_1:
            if self.game_board[4] == ' ':
                self.weighted_board_block[4] += 1
        if self.game_board[4] == self.player.player_1 and self.game_board[6] == self.player.player_1:
            if self.game_board[5] == ' ':
                self.weighted_board_block[5] += 1

        if self.game_board[7] == self.player.player_1 and self.game_board[8] == self.player.player_1:
            if self.game_board[9] == ' ':
                self.weighted_board_block[9] += 1
        if self.game_board[8] == self.player.player_1 and self.game_board[9] == self.player.player_1:
            if self.game_board[7] == ' ':
                self.weighted_board_block[7] += 1
        if self.game_board[7] == self.player.player_1 and self.game_board[9] == self.player.player_1:
            if self.game_board[8] == ' ':
                self.weighted_board_block[8] += 1
        
        #Vertical weights
        if self.game_board[1] == self.player.player_1 and self.game_board[4] == self.player.player_1:
            if self.game_board[7] == ' ':
                self.weighted_board_block[7] += 1
        if self.game_board[4] == self.player.player_1 and self.game_board[7] == self.player.player_1:
            if self.game_board[1] == ' ':
                self.weighted_board_block[1] += 1
        if self.game_board[1] == self.player.player_1 and self.game_board[7] == self.player.player_1:
            if self.game_board[4] == ' ':
                self.weighted_board_block[4] += 1

        if self.game_board[2] == self.player.player_1 and self.game_board[5] == self.player.player_1:
            if self.game_board[8] == ' ':
                self.weighted_board_block[8] += 1
        if self.game_board[5] == self.player.player_1 and self.game_board[8] == self.player.player_1:
            if self.game_board[2] == ' ':
                self.weighted_board_block[2] += 1
        if self.game_board[2] == self.player.player_1 and self.game_board[8] == self.player.player_1:
            if self.game_board[5] == ' ':
                self.weighted_board_block[5] += 1

        if self.game_board[3] == self.player.player_1 and self.game_board[6] == self.player.player_1:
            if self.game_board[9] == ' ':
                self.weighted_board_block[9] += 1
        if self.game_board[6] == self.player.player_1 and self.game_board[9] == self.player.player_1:
            if self.game_board[3] == ' ':
                self.weighted_board_block[3] += 1
        if self.game_board[3] == self.player.player_1 and self.game_board[9] == self.player.player_1:
            if self.game_board[6] == ' ':
                self.weighted_board_block[6] += 1

        #Diagonal weights
        if self.game_board[5] == self.player.player_1:
            if self.game_board[1] == self.player.player_1:
                self.weighted_board_block[9] += 1
            if self.game_board[3] == self.player.player_1:
                self.weighted_board_block[7] += 1
            if self.game_board[7] == self.player.player_1:
                self.weighted_board_block[3] += 1
            if self.game_board[9] == self.player.player_1:
                self.weighted_board_block[1] += 1

        # self.display_board_block()
                

    def display_board(self):
        weighted_board_1 = self.weighted_board_win
        print("Win Table")
        print(f"{weighted_board_1[7]}" + ' |' +
              f"{weighted_board_1[8]}" + ' |' + f"{weighted_board_1[9]}")
        print('--+--+--')
        print(f"{weighted_board_1[4]}" + ' |' +
              f"{weighted_board_1[5]}" + ' |' + f"{weighted_board_1[6]}")
        print('--+--+--')
        print(f"{weighted_board_1[1]}" + ' |' +
              f"{weighted_board_1[2]}" + ' |' + f"{weighted_board_1[3]}")
        
        weighted_board_2 = self.weighted_board_block
        print("Blocking Table")
        print(f"{weighted_board_2[7]}" + ' |' +
              f"{weighted_board_2[8]}" + ' |' + f"{weighted_board_2[9]}")
        print('--+--+--')
        print(f"{weighted_board_2[4]}" + ' |' +
              f"{weighted_board_2[5]}" + ' |' + f"{weighted_board_2[6]}")
        print('--+--+--')
        print(f"{weighted_board_2[1]}" + ' |' +
              f"{weighted_board_2[2]}" + ' |' + f"{weighted_board_2[3]}")

    def display_board_win(self):
        weighted_board_1 = self.weighted_board_win
        print("Win Table")
        print(f"{weighted_board_1[7]}" + ' |' +
              f"{weighted_board_1[8]}" + ' |' + f"{weighted_board_1[9]}")
        print('--+--+--')
        print(f"{weighted_board_1[4]}" + ' |' +
              f"{weighted_board_1[5]}" + ' |' + f"{weighted_board_1[6]}")
        print('--+--+--')
        print(f"{weighted_board_1[1]}" + ' |' +
              f"{weighted_board_1[2]}" + ' |' + f"{weighted_board_1[3]}")

    def display_board_block(self):
        weighted_board_2 = self.weighted_board_block
        print("Blocking Table")
        print(f"{weighted_board_2[7]}" + ' |' +
              f"{weighted_board_2[8]}" + ' |' + f"{weighted_board_2[9]}")
        print('--+--+--')
        print(f"{weighted_board_2[4]}" + ' |' +
              f"{weighted_board_2[5]}" + ' |' + f"{weighted_board_2[6]}")
        print('--+--+--')
        print(f"{weighted_board_2[1]}" + ' |' +
              f"{weighted_board_2[2]}" + ' |' + f"{weighted_board_2[3]}")

    def computer_placement_win(self):
        self.smart_choice_cpu()
        self.sorted_weights_win = sorted(self.weighted_board_win.items(), key=operator.itemgetter(1), reverse=True) #arranges locations with highest weight
        
        sorted_weights_win_list = []
        for x in range(len(self.sorted_weights_win)):
            a,b = self.sorted_weights_win[x]
            sorted_weights_win_list.append([a, b])

        # print("Wins")
        # print(sorted_weights_win_list)
        return sorted_weights_win_list

    def computer_placement_block(self):
        self.smart_choice_player()
        self.sorted_weights_block = sorted(self.weighted_board_block.items(), key=operator.itemgetter(1), reverse=True) #arranges locations with highest weight
        
        sorted_weights_block_list = []
        for x in range(len(self.sorted_weights_block)):
            a,b = self.sorted_weights_block[x]
            sorted_weights_block_list.append([a, b])

        # print("Block")
        # print(sorted_weights_block_list)
        return sorted_weights_block_list

'''                                    CHANGING THINGS UP                                             '''

def play_game(game, players, computer):
    mark = []
    mark = players
    difficulty = game.difficulty
    while not game.game_over:

        if game.move < 1:  #Player Turn

            computer.weight_reset()
            # computer.display_board_win()
            # computer.display_board_block()

            choice = game.user_input(mark[0])
            game.game_board[choice] = mark[0]
            game.display_board()
            game.move += 1
            game.check_win(mark[0])
            if game.has_won == True:
                game.game_over = True
                break
            if game.is_board_full():
                game.game_over = True
                print("Game board is full")
                break

        elif game.move == 1:    #Computer Turn
            
            # computer.weight_reset()
            # computer.weighted_board_win = computer.weighted_board_defualt
            # computer.weighted_board_win = computer.weighted_board_defualt
            # computer.display_board_win()
            # computer.display_board_block()

            # computer.display_board()

            win = computer.computer_placement_win()
            block = computer.computer_placement_block()

            dif_val = random.randint(1, 10)
            played = 0
            
            if dif_val <= difficulty: #Succeeds difficulty setting
                
                
                for x in range(len(win)): #Chooses places with win condition
                    if win[x][1] >= 1:
                        game.game_board[win[x][0]] = mark[1]
                        print(f"Computer plays {mark[1]} at location {win[x][0]}")
                        played += 1
                        break
                
                if played == 0:
                    for x in range(len(block)): #Chooses places with block condition
                        if block[x][1] >= 1:
                            game.game_board[block[x][0]] = mark[1]
                            print(f"Computer plays {mark[1]} at location {block[x][0]}")
                            break

                        elif block[x][1] == 0: #Chooses random location

                            while True:
                                rand = random.randint(1,9)
                                if game.game_board[rand] == ' ':
                                    game.game_board[rand] = mark[1]
                                    print(f"Computer plays {mark[1]} at location {rand}")
                                    break
                            break
                
            elif dif_val > difficulty:
                while True:
                    rand = random.randint(1,9)
                    if game.game_board[rand] == ' ':
                        game.game_board[rand] = mark[1]
                        print(f"Computer plays {mark[1]} at location {rand}")
                        break
                                    

            game.display_board()
            game.move -= 1
            game.check_win(mark[1])
            if game.has_won == True:
                game.game_over = True
                break
            if game.is_board_full():
                game.game_over = True
                print("Game board is full")
                break

def main():
    game = Game() #defualts and difficulty
    player = Player() #player tokens
    player.player1()
    computer = Cpu(game, player) #Creates computer

    game.display_board()

    play_game(game, player.player1(), computer)

main()