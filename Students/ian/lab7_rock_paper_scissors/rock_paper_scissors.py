"""
Let's play rock-paper-scissors with the computer.

    The computer will ask the user for their choice (rock, paper, scissors)
    The computer will randomly choose rock, paper or scissors
    Determine who won and tell the user

Let's list all the cases:

    rock vs rock (tie)
    rock vs paper
    rock vs scissors
    paper vs rock
    paper vs paper
    paper vs scissors
    scissors vs rock
    scissors vs paper
    scissors vs scissors

"""

import random

RPS = ["rock", "paper", "scissor"]


class RockPaperScissor:
    def __init__(self, p1, p2):
        self.score =[[p1,0], [p2, 0]]

    def rockPaperScissor(self,a, b):
        print(a,b)
        if a not in RPS or b not in RPS:
            print("bad entry")
            return False
        if a == b:
            print("tie")
            return False
        elif a == "rock" and b == "paper" or a == "paper" and b == "scissor" or a == "scissor" and b == "paper":
            return self.recordWin(1)
        return self.recordWin(0)

    def recordWin(self,name):
        if self.score[name][1] >= 0:
            self.score[name][1] = self.score[name][1] + 1
            print("Score for ", self.score[name][0])
            if(self.score[name][1] > 2):
                print("Game over ", self.score[name][0], " wins")
                return True
        return False 
    
    def randomChoice(self):
        return random.choice(RPS)


def main():
    try:
        done = False
        rps = RockPaperScissor("player", "computer")
        while not done:
            choice = input("Enter rock, paper, or scissor: ").lower()
            comp_choice = rps.randomChoice()
            done =rps.rockPaperScissor(choice, comp_choice)
       
    except Exception as err:
        print("error", err)
        exit(1)



if __name__ == '__main__':
    main()