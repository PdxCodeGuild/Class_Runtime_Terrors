import random

def random_picks():
    number_of_picks = 0
    picks = [] # initializes list of number picks list
    while number_of_picks < 6:
        picks.append (random.randrange(1, 100))
        number_of_picks += 1
    return (picks)

def determine_matches(winner_list, player_list):
    matches = 0 # initialize variable to track number of matching numbers
    number_list_index = 0 # initialize variable to index through lists of winning numbers and player numbers
    winning_number_tally = [] # initialized list to track the winning numbers

    # loops through each index of the computer's and player's list to check for matches
    while number_list_index <6:
        if winner_list [number_list_index] == player_list [number_list_index]:
            matches += 1 # increments number of matches of a match is found
            winning_number_tally.append (winner_list [number_list_index]) # records matched numbers (for future use)
        number_list_index += 1
    return (matches) # returns number of matches


def payout_table (matches):
    winning_amounts = {
        0:        0,
        1:        4,
        2:        7,
        3:      100,
        4:    50000,
        5:  1000000,
        6: 25000000
    }
    winning_payout = winning_amounts [matches]
    return winning_payout

def main():
    winnings = 0 # initializes winning tally
    spendings = 0 # initializes spending tally
    times_played = 0 # initializes number of times played so far
    number_of_plays = 100000 # determines number of times to play the game
    winner_numbers = random_picks() # calls function to generate and return computer's numbers
    
    
    while times_played < number_of_plays:
        player_numbers = random_picks() # calls function to generate and return player's numbers
        matches = determine_matches (winner_numbers, player_numbers) # calls function to determine and return number of matches
        winning_payout = payout_table (matches) # returns the payout based on the number of matches
        winnings += winning_payout # adds payout to winning tally
        winnings_formatted = ("{:,}".format(winnings)) # formats winning tally with commas
        spendings += 2 # adds ticket cost to spending tally
        spendings_formatted = ("{:,}".format(spendings)) # formats spending tally with commas
        times_played += 1 # increments counter for number of times played
        cost_bennefit = winnings - spendings
        cost_bennefit_formatted = ("{:,}".format(cost_bennefit))
        roi = cost_bennefit/spendings

    print (f'\nYou played {times_played} times.\n')
    print (f'You spent ${spendings_formatted}.\n')
    print (f'You won ${winnings_formatted}.\n')
    print (f'Your final tally is ${cost_bennefit_formatted}.\n')
    print (f'Your ROI is {roi}')



main()