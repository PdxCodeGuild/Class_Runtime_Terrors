Purple.Discord.com

Project Overview:

The purpose of this project is to create a website to manage and invite a discord bot I am developing. To start with, the site will be capable of creating and managing reminder DM's (Discord Messages). The bot will be able to send a message to a user with the bot enabled on a server they are a member of, at a specific time with a custom message. Further functionanility will be made as more features to the bot are added over time. There will be a home page with a quick overview of what the bot can do, an invite page to bring the bot to a server you manage, and a profile page to manage bot actions specific to the user. All of this will run on a discord login

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

Data Model
id - Users public Discord ID
avatar - Users Discord Avatar (just the Identification code to grab from Discord)
Time and Date - Keeps track of the time and date so messages can be sent when there is a match
Message Content - The message to be sent to the user when Time and Date match.