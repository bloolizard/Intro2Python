# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# Edwin Villanueva 10/26/2013

import simplegui
import random
import math


# initialize global variables used in your code
num_range = 100
secretNumber = 0
num_lives = 0

beer = """
        ~  ~
      ( o )o)
     ( o )o )o)
   (o( ~~~~~~~~o
   ( )' ~~~~~~~'
   ( )|)       |-.
     o|     _  |-. \
     o| |_||_) |  \ \
      | | ||_) |   | |
     o|        |  / /
      |        |." "
      |        |- '
      .========.   mb

"""



# helper function to start and restart the game
def new_game():
    frame.start()
    print "Game started..."
    range100() #range100 is the default
    


# define event handlers for control panel
def range100():
    global secretNumber
    global num_lives
    print "Range is [0, 100)"
    secretNumber = random.randrange(0, 100)
    print "Secret number has been changed."
    num_lives = math.ceil(math.log(100,2))
    print "Number of lives has been set to", int(num_lives)
    

def range1000():
    global secretNumber
    global num_lives
    print "Range is [0, 1000)"
    secretNumber = random.randrange(0,1000)
    print "Secret number has been changed."
    num_lives = math.ceil(math.log(1000,2))
    print "Number of lives has been set to", int(num_lives)
    
def input_guess(guess):
    global num_lives
    if guess:
        guess = int(guess)
    print "The guess is:",guess 
    # main game logic goes here
    if num_lives > 0:
        if guess == secretNumber:
            print "success!! You win!!"
            print beer
            print "Restarting the game... because you did so well!"
            new_game()
        elif guess > secretNumber:
            num_lives -= 1
            print "Lower"
            print "You have", int(num_lives), "lives remaining." 
        elif guess < secretNumber:
            num_lives -= 1
            print "Higher"
            print "You have", int(num_lives), "lives remaining." 
        else:
            print "Invalid input.  Ugh guess again."
    else:
        print "Death. Game must restart =("
        new_game()
         

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)



# call new_game and start frame
new_game()


# always remember to check your completed program against the grading rubric
