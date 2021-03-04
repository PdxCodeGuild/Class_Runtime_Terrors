Purple.Discord.com

Project Overview:

<<<<<<< HEAD
<<<<<<< HEAD
The point of this application is to be able to play the game of Checkers against a multi level difficulty AI, and, time permitting, another player (or vice versa). 
=======
The purpose of this project is to create a website to manage and invite a discord bot I am developing. To start with, the site will be capable of creating and managing reminder DM's (Discord Messages). The bot will be able to send a message to a user with the bot enabled on a server they are a member of, at a specific time with a custom message. Further functionanility will be made as more features to the bot are added over time. There will be a home page with a quick overview of what the bot can do, an invite page to bring the bot to a server you manage, and a profile page to manage bot actions specific to the user. All of this will run on a discord login
>>>>>>> 30d074996118eabf39297f0c7f6137047f4132b6
=======
The purpose of this project is to create a website to manage and invite a discord bot I am developing. To start with, the site will be capable of creating and managing reminder DM's (Discord Messages). The bot will be able to send a message to a user with the bot enabled on a server they are a member of, at a specific time with a custom message. Further functionanility will be made as more features to the bot are added over time. There will be a home page with a quick overview of what the bot can do, an invite page to bring the bot to a server you manage, and a profile page to manage bot actions specific to the user. All of this will run on a discord login
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984

The project will Utilize Django, Discord API, and sqlite3 (And maybe migrate to PostgreSQL since a web tutorial I am using to help guide me recommends it).

Functionality:

Home Page - Displays Key Bot Features
          - Log In Function
          - Bot Invite Link

Profile Page
          - Displays User Relevent Data (Bot Alarms)

Bot Management Page
          - Displays User Alarms
          - Allows for Creating, Deleting, and Editing Alarms.

<<<<<<< HEAD
<<<<<<< HEAD
As outlined above, the app will provide the game of Checkers, with the goal of it allowing for PvP type games but will start with just AI controls to begin with (Or vice versa, with PvP being worked on first, then the AI games).

Main Page - Portal site for starting a game and navigating to the highscores page
          - Will display the top scores for each category:
            - Shortest Match
            - Least Turns To Win
            - Least Pieces Lost

Game Page - Start match making
          - Display game board
          - Space for game chat (time permitting)

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
=======
=======
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984
Data Model
id - Users public Discord ID
avatar - Users Discord Avatar (just the Identification code to grab from Discord)
Time and Date - Keeps track of the time and date so messages can be sent when there is a match
<<<<<<< HEAD
Message Content - The message to be sent to the user when Time and Date match.
>>>>>>> 30d074996118eabf39297f0c7f6137047f4132b6
=======
Message Content - The message to be sent to the user when Time and Date match.
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984
