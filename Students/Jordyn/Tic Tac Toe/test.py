class Game:
    def __init__(self):
        self.move = 0
        self.board_full = False
        self.game_over = False
        self.has_won = False
        self.valid_input = False
        self.game_board = {7: " ", 8: " ", 9: "O",
                           4: " ", 5: " ", 6: "O",
                           1: "X", 2: "X", 3: " "}

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

    def play_game(self, players):
        mark = []
        mark = players
        while not self.game_over:
            if self.move < 1:  
                choice = self.user_input(mark[0])
                self.game_board[choice] = mark[0]
                self.display_board()
                self.move += 1
                self.check_win(mark[0])
                if self.has_won == True:
                    self.game_over = True
                    break
                if self.is_board_full():
                    self.game_over = True
                    print("Game board is full")
                    break

            elif self.move == 1:
                choice = self.user_input(mark[1])
                self.game_board[choice] = mark[1]
                self.display_board()
                self.move -= 1
                self.check_win(mark[1])
                if self.has_won == True:
                    self.game_over = True
                    break
                if self.is_board_full():
                    self.game_over = True
                    print("Game board is full")
                    break

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
        self.weighted_board = {7: 0, 8: 0, 9: 0,
                               4: 0, 5: 0, 6: 0,
                               1: 0, 2: 0, 3: 0}
        self.game_board = game.game_board
        self.player = player

    def smart_choice_cpu(self):
        
        print(self.player.player_2, "<<< Computer Token")
        
        #if middle space is open, take it
        if self.game_board[5] == ' ':
            self.weighted_board[5] += 5

        #Horizontal weights
        if self.game_board[2] == self.player.player_2 and self.game_board[3] == self.player.player_2:
            if self.game_board[1] == ' ':
                self.weighted_board[1] += 1
        if self.game_board[1] == self.player.player_2 and self.game_board[2] == self.player.player_2:
            if self.game_board[3] == ' ':
                self.weighted_board[3] += 1
        if self.game_board[1] == self.player.player_2 and self.game_board[3] == self.player.player_2:
            if self.game_board[2] == ' ':
                self.weighted_board[2] += 1

        if self.game_board[4] == self.player.player_2 and self.game_board[5] == self.player.player_2:
            if self.game_board[6] == ' ':
                self.weighted_board[6] += 1
        if self.game_board[5] == self.player.player_2 and self.game_board[6] == self.player.player_2:
            if self.game_board[4] == ' ':
                self.weighted_board[4] += 1
        if self.game_board[4] == self.player.player_2 and self.game_board[6] == self.player.player_2:
            if self.game_board[5] == ' ':
                self.weighted_board[5] += 1

        if self.game_board[7] == self.player.player_2 and self.game_board[8] == self.player.player_2:
            if self.game_board[9] == ' ':
                self.weighted_board[9] += 1
        if self.game_board[8] == self.player.player_2 and self.game_board[9] == self.player.player_2:
            if self.game_board[7] == ' ':
                self.weighted_board[7] += 1
        if self.game_board[7] == self.player.player_2 and self.game_board[9] == self.player.player_2:
            if self.game_board[8] == ' ':
                self.weighted_board[8] += 1
        
        #Vertical weights
        if self.game_board[1] == self.player.player_2 and self.game_board[4] == self.player.player_2:
            if self.game_board[7] == ' ':
                self.weighted_board[7] += 1
        if self.game_board[4] == self.player.player_2 and self.game_board[7] == self.player.player_2:
            if self.game_board[1] == ' ':
                self.weighted_board[1] += 1
        if self.game_board[1] == self.player.player_2 and self.game_board[7] == self.player.player_2:
            if self.game_board[4] == ' ':
                self.weighted_board[4] += 1

        if self.game_board[2] == self.player.player_2 and self.game_board[5] == self.player.player_2:
            if self.game_board[8] == ' ':
                self.weighted_board[8] += 1
        if self.game_board[5] == self.player.player_2 and self.game_board[8] == self.player.player_2:
            if self.game_board[2] == ' ':
                self.weighted_board[2] += 1
        if self.game_board[2] == self.player.player_2 and self.game_board[8] == self.player.player_2:
            if self.game_board[5] == ' ':
                self.weighted_board[5] += 1

        if self.game_board[7] == self.player.player_2 and self.game_board[8] == self.player.player_2:
            if self.game_board[9] == ' ':
                self.weighted_board[9] += 1
        if self.game_board[8] == self.player.player_2 and self.game_board[9] == self.player.player_2:
            if self.game_board[7] == ' ':
                self.weighted_board[7] += 1
        if self.game_board[7] == self.player.player_2 and self.game_board[9] == self.player.player_2:
            if self.game_board[8] == ' ':
                self.weighted_board[8] += 1

        # #Diagonal weights
        if self.game_board[5] == self.player.player_2:
            if self.game_board[1] == self.player.player_2:
                if self.game_board[9] == ' ':
                    self.weighted_board[9] += 1
            if self.game_board[3] == self.player.player_2:
                if self.game_board[7] == ' ':
                    self.weighted_board[7] += 1
            if self.game_board[7] == self.player.player_2:
                if self.game_board[3] == ' ':
                    self.weighted_board[3] += 1
            if self.game_board[9] == self.player.player_2:
                if self.game_board[1] == ' ':
                    self.weighted_board[1] += 1
        
        return self.weighted_board
        
    def smart_choice_player(self):
        print(self.player.player_1, "<<< Player Token")

        #Horizontal weights
        if self.game_board[2] == self.player.player_1 and self.game_board[3] == self.player.player_1:
            if self.game_board[1] == ' ':
                self.weighted_board[1] += 1
        if self.game_board[1] == self.player.player_1 and self.game_board[2] == self.player.player_1:
            if self.game_board[3] == ' ':
                self.weighted_board[3] += 1
        if self.game_board[1] == self.player.player_1 and self.game_board[3] == self.player.player_1:
            if self.game_board[2] == ' ':
                self.weighted_board[2] += 1

        if self.game_board[4] == self.player.player_1 and self.game_board[5] == self.player.player_1:
            if self.game_board[6] == ' ':
                self.weighted_board[6] += 1
        if self.game_board[5] == self.player.player_1 and self.game_board[6] == self.player.player_1:
            if self.game_board[4] == ' ':
                self.weighted_board[4] += 1
        if self.game_board[4] == self.player.player_1 and self.game_board[6] == self.player.player_1:
            if self.game_board[5] == ' ':
                self.weighted_board[5] += 1

        if self.game_board[7] == self.player.player_1 and self.game_board[8] == self.player.player_1:
            if self.game_board[9] == ' ':
                self.weighted_board[9] += 1
        if self.game_board[8] == self.player.player_1 and self.game_board[9] == self.player.player_1:
            if self.game_board[7] == ' ':
                self.weighted_board[7] += 1
        if self.game_board[7] == self.player.player_1 and self.game_board[9] == self.player.player_1:
            if self.game_board[8] == ' ':
                self.weighted_board[8] += 1
        
        #Vertical weights
        if self.game_board[1] == self.player.player_1 and self.game_board[4] == self.player.player_1:
            if self.game_board[7] == ' ':
                self.weighted_board[7] += 1
        if self.game_board[4] == self.player.player_1 and self.game_board[7] == self.player.player_1:
            if self.game_board[1] == ' ':
                self.weighted_board[1] += 1
        if self.game_board[1] == self.player.player_1 and self.game_board[7] == self.player.player_1:
            if self.game_board[4] == ' ':
                self.weighted_board[4] += 1

        if self.game_board[2] == self.player.player_1 and self.game_board[5] == self.player.player_1:
            if self.game_board[8] == ' ':
                self.weighted_board[8] += 1
        if self.game_board[5] == self.player.player_1 and self.game_board[8] == self.player.player_1:
            if self.game_board[2] == ' ':
                self.weighted_board[2] += 1
        if self.game_board[2] == self.player.player_1 and self.game_board[8] == self.player.player_1:
            if self.game_board[5] == ' ':
                self.weighted_board[5] += 1

        if self.game_board[7] == self.player.player_1 and self.game_board[8] == self.player.player_1:
            if self.game_board[9] == ' ':
                self.weighted_board[9] += 1
        if self.game_board[8] == self.player.player_1 and self.game_board[9] == self.player.player_1:
            if self.game_board[7] == ' ':
                self.weighted_board[7] += 1
        if self.game_board[7] == self.player.player_1 and self.game_board[9] == self.player.player_1:
            if self.game_board[8] == ' ':
                self.weighted_board[8] += 1

        #Diagonal weights
        if self.game_board[5] == self.player.player_1:
            if self.game_board[1] == self.player.player_1:
                self.weighted_board[9] += 1
            if self.game_board[3] == self.player.player_1:
                self.weighted_board[7] += 1
            if self.game_board[7] == self.player.player_1:
                self.weighted_board[3] += 1
            if self.game_board[9] == self.player.player_1:
                self.weighted_board[1] += 1
        
        return self.weighted_board

    def display_board(self):
        weighted_board = self.weighted_board
        print(f"{weighted_board[7]}" + ' |' +
              f"{weighted_board[8]}" + ' |' + f"{weighted_board[9]}")
        print('--+--+--')
        print(f"{weighted_board[4]}" + ' |' +
              f"{weighted_board[5]}" + ' |' + f"{weighted_board[6]}")
        print('--+--+--')
        print(f"{weighted_board[1]}" + ' |' +
              f"{weighted_board[2]}" + ' |' + f"{weighted_board[3]}")

def main():
    player = Player()
    player.player1()
    game = Game()
    player.player1()



    computer = Cpu(game, player)
    computer.game_board = computer.smart_choice_cpu()
    computer.game_board = computer.smart_choice_player()
    computer.display_board()
    game.display_board()


main()
