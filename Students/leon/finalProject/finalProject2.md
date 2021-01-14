# PROJECT Prometheus Process

### Capstone Proposal - second attempt

---
---
## OVERVIEW: 

This project will create a space where users can establish goals according to 'the Prometheus Process' - a strategic planning technique originally deployed for organizational change, and now also used in personal goal-setting approaches. The Prometheus Process involves 4 steps:
1. Start at the End
2. Daily Diligence
3. Map Systems
4. Action Plan

---
## FUNCTIONALITY

The generic landing page will be rather bland - there is not much to do but sign-up, or log-in. Once a user-account is created, the user will be given a personal landing page where they can go to a profile page, log-out, and write a "Future Picture" - a description of their goal at the fulfilled state. Once the "Future Plan" has been developed it will be displayed on this page. The user will be able to upload media files to this page in a designated space which will help them imagine the end-goal state, or motivate them. Other areas will be linked to this "Future Picture" page.

"Daily Drills" links to a simple blog application; user can add an entry or read through the list of posts.  It is used for journaling their path towards this goal. It is not shared with other users or externally - we want the user to be honest with themselves, not get trained by robots to collect "thumbs up" stickers. The users objective is to take a few minutes each day to reflect on the end-state of their goal. It is recommended to read the "Future Picture" - aloud if possible - and then just free-write, or describe something specific about this Picture which sticks in your mind just now. But this Journal space is also useful for just basic journalling on this one specific topic - frustrations, fears, "little vics", etc. <!-- hmm... should the Daily Drills page have a countdown clock, based on the deadline of the Future Picture, ticking at the top of this page? keep on focused or too distracting?? -->

"Map systems" is another link that will let the user upload a file of their 'ecosystem' - which is their present environment that includes people, processes, infrastructure and other resources that are part of or need to be part of their strategic plan in order to achieve their goal. The idea here is to just realize what you need in order to achieve what you want, and figure out what is in the way or holding you back from doing it. This is meant to be a creative and visual experience that SHOWS where the problems are and where the help is. 

"Action Plan" links to a "todo list" application where the user can input the steps they must take to achieve their goal, and mark them off as they go. At a more complex development of this site, there will be lightweight project management tools to assist with taking information from the map and turning it into a "todo list" - with short term and long term objectives, and scheduled check-ins that auto-email the user at the due-date for a self-evaluation. (actually this might be a good idea for the Daily Drills too - daily reminder to take 5 and think about your goal at a user-defined time.) 

"Resource Page" links to another blog-like app, but this one is specifically for collecting resources the user found on their journey and wants to keep in this space for reference, or may want to share with other users in a future-development feature of this site. 

---
## DATA MODEL

Users will need to be able to create unique profiles in order to login and etc. and prevent other users from seeing their personal space.

User account model will have username (unique), email (optional) and password.

Future Picture data-model will include title, pub-date, start-date, deadline, end-date, success (boolean), author (user-profile auto-associated), and a text-field. 

Enhancements area will house the users' media files so there is probably a data-model for this with like, auhtor, pub-date, media-type, file-size, or something like that. 

Daily Drills data-model will include text, pub-date and author (user-profile auto-associated).

System Map will have an uploader for an image file which will then display that image. 

Action Plan model will have the same functionality as a traditional to-do list. 

Resource Page will have the same model structure as a tradition blog: title, pub_date, author, text. 


---
## Schedule

24 JAN: have all labs finished
25 JAN: begin work on Capstone
31 JAN: finish user account login/logout and personal landing page elements
01 FEB: begin work on Action Plan app (to-do list page)
08 FEB: begin work on Daily Drills and Resources mini-blog apps
15 FEB: begin work on System Map page and Media Resources enhancement feature of personal landing page
22 FEB: begin working on making it prettier

............................
++++++++++++++++++++++++++++
