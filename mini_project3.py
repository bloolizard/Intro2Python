# template for "Stopwatch: The Game"
# by Edwin Villanueva
# last updated 10/30/2013

import simplegui
import random
import math
import time

# define global variables

minutes = 0 
seconds = 0
milliseconds = 0
gtime = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def new_game():
    frame.start()
    print "Game has started..."




    
    
def format(t):
    global gtime
    if t:
        gtime = int(t)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer.start()
    print "Starting timer..."

def stop_timer():
    timer.stop()
    print "Stopping timer..."

def reset_timer():
    global gtime
    gtime = 0
    print "Timer has been reset..."

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global gtime
    gtime += 1
    print int(gtime)
    
timer = simplegui.create_timer(10, timer_handler)


# define draw handler
def draw(canvas):
    canvas.draw_text(str(int(gtime)), [100, 100], 24, "White")
    
# create frame
frame = simplegui.create_frame("Time in'", 200, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start Timer", start_timer, 200)
frame.add_button("Stop Timer", stop_timer, 200)
frame.add_button("Reset Timer", reset_timer, 200)
frame.add_input("Format", format, 200)

# start frame
new_game()

# Please remember to review the grading rubric
