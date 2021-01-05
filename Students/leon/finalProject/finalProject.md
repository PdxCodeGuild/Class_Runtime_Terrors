# Capstone Proposal

---------------------------
## PROJECT: At the Crossroads

## OVERVIEW: 
'At the Crossroads' will simulate a common situation in PENDRAGON role-playing games: a Player-Knight must joust against all comers for a month at some fixed spot where he is likely to encounter other Knights.<br>

To do this, the program will generate the Player Knight (PK), then determine the number of encounters. It will then generate a random opponent for each encounter. The encounters will be evaluated by simulating actual Pendragon rules - except that I will add elements observed in "Full Metal Jousting": each joust will consist of three tries, with 1pt for a touch, 3pts for breaking a lance, and 5pts for unhorsing. The Wins and Losses will be displayed after all jousts, as well as a final points (this roughly corresponds to the amount of Glory won). <br>

The major problem for the GM is coming up with anywhere from 7 to 20 random knights on the fly - without details like "homeland", "name", and "Coat of arms" this adventure becomes a grind instead of an interesting opportunity to introuduce some flavor that maintains the spirit of the game. This program will use some version of SQL (lots of tables) and Django to allow a GM to generate these details with little effort. Having even a small list of facts about the opponent gives the GM a springboard for banter, gossip, or other quirks which draws the Player into engaging the encounter with more than quick toss of the dice.<br> 

## FUNCTIONALITY

The homepage will be somewhat empty except for a description and a 'get started' button; there will be background imagery, and a navigation bar. <br>

Having selected 'get started', the user will be asked to choose between "Backroads", "Crossroads" and "Highway" - these determine the number of encounters. (With this information, the computer can begin generating the Opponents).<br>

The PK will be generated with an adjusted set of rules, reflecting the RPG which assumes the PK are above-average - but by no means "supermen". A choice of homelands (or perhaps just a default for now...) determines which library a name is to be randomly pulled from; and "rolls" (carefully modulated random numbers simulating a curve to that of the RPG) for basic stats and a SKILL. The generator will display a written character portfolio including Name, Homeland, and a description of the Knight's coat-of-arms (a suggested meaning based on the heraldry may display as a mouseover effect if I have time).<br>

After character creation, the PK will be reduced to a name, a SKILL, a PTS and a SCORE block under the square where his coat of arms will sit (for now, a text block) in the upper left corner. An opposing block in the upper right will show the coat of arms, name, homeland, and SKILL of the opponent. In the middle of the screen are two dodecahedrons (20 sided die), blank. On each round (displayed as a flash message) the die will show some random number. A new flash message will declare who is the winner of this round. The winner is determined by using the roll compared to the SKILL to determine a CRIT, HIT or MISS. On a HIT, the 'unseen' STATS of SIZ and STR are computed for DMG - plus a CHARGE bonus, of course. The DMG is compared to the opponent's KD (knockdown is computed by SIZ and CON). If (DMG > KD): the opponent is unhorsed (5pts). else: a Touch (1pt). On a CRIT, the lance breaks (3pts), and a 2nd SKILL Roll is made. If this one also scores a HIT, the opponent is ALSO unhorsed. After all three rounds, the PTS will aggregate and the SCORE will remain on a LOSS or advance by 1 on a WIN.<br>

After all jousts have been run, the character's win/loss record and final points are displayed.<br>

## DATA MODEL

To accomplish this, I will need at least 1 HOMELANDS list with all available LANDS; 1 NAMES list for the common names of the Default Homeland (PK) plust at least 1 list sampling common names for the HOMELANDS (to be expanded later); a set of lists comprising the basic options available to describe a coat of arms (FIELD, ORDINARY, CHARGE; Metals, Tinctures) and a function which, when called, reliably creates a simple coat of arms. A set of functions which, when called, will generate each of the necessary STATS (plus HOMELAND +/-) and store each of them in a unique and callable data-set so they can be compared against each other. A function which describes the rules of the game.

## Schedule

15 JAN = prime stats generator
20 JAN = name generator
01 FEB = non-PK generator w/o heraldry
15 FEB = basic rules for a 1-off joust between 2 random non-PK's
26 FEB = functional PK vs non-PK 'At the Crossroads' barebones package





















