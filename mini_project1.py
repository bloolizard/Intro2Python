# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "not a valid number"
    
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "not a valid name"
    # convert name to number using if/elif/else
    # don't forget to return the result!

def rpsls(name):
    print "Player chooses " + name
    player_number = name_to_number(name)
    
    comp_number = random.randrange(0,5)
    print "Computer chooses " + number_to_name(comp_number)
    
    # rule: beat counterclockwise opponents, lose to clockwise opponents
    # e.g. 0 beats 4 and 3 but loses to 1 and 2
    # e.g. 1 beats 0 and 4 but loes to 2 and 3
    
    winner = player_number - comp_number
    if winner < 0:# number is negative
        winner = winner + 5
    
    if winner == 1 or winner == 2:#first item wins
        print "Player wins!"
    elif winner == 3 or winner == 4:#second item wins
        print "Computer wins!"
    else:
        print "It's a tie.  Be friends =)."
        
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric