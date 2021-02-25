checkers.game.com

Project Overview:

The point of this application is to be able to play the game of Checkers against a multi level difficulty AI, and, time permitting, another player (or vice versa). 

There will be a user login function to store data on scores like:
 - Time spent in the game
 - Total number of turns to achieve victory
 - Total pieces lost (Players and enemies)

as well as general information such as:
 - Time and Date of match played
 - Comments on the game (probably only for player vs player interaction)
 - Total Games played
 - Wins and Loses (Both AI and PvP)

I'll be using Django and until I learn of a better alternative, the basic SQL database it employs. That is something for the future however.


Functionality:

As outlined above, the app will provide the game of Checkers, with the goal of it allowing for PvP type games but will start with just AI controls to begin with (Or vice versa, with PvP being worked on first, then the AI games).

Main Page - Portal site for starting a game and navigating to the highscores page
          - Will display the top scores for each category:
            - Shortest Match
            - Least Turns To Win
            - Least Pieces Lost

Game Page - Start match making
          - Display game board
          - Space for game chat (time permitting) (Saved for last)

Highscore - Display the top 10 of each score type:
            - Shortest Match
            - Least Turns To Win
            - Least Pieces Lost

Profile P.- Display personal information:
            - Games Played
              - Wins
              - Losses
              - Ties(?)
            - Games of type (AI/PvP)
            - Game History
              - Against Who
                - Win
                - Lose
                - Score
            - Change Password
            - Change Email
            - Change Profile Image (?)
            - Achievements (?)


Data Model:
Checker Board + Pieces
Username + Password
(maybe) Profile Picture
Total Games
Total Wins
Total Loses
Total Pieces lost
Total Kings
Players Matched (And how many times of same player)

Schedule:
¯\_(ツ)_/¯

==========================================================

*** Items listed with "(?)" are features with low priority and will be added, time permitting.