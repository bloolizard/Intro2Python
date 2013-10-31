# template for "Stopwatch: The Game"
# by Edwin Villanueva
# last updated 10/31/2013

import simplegui
import random
import math
import time

# define global variables

gtime = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def new_game():
    frame.start()
    print "Game has started..."




    
# return a string of the form A:BC.D    
def format(t):
    t = int(t)
    D = t % 10
    C = t / 10 % 10
    B = t / 100 % 10
    A = t / 1000 % 10
    if B > 5:
        B = B % 6
        A += 1
    ftime =  "%d:%d%d.%d" % (A,B, C, D)
    return ftime


    
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

def set_custom_time(time):
    global gtime
    try:
        time = int(time)
        gtime = time
        print "Time has been updated"
    except:
        print "Please enter a valid input =(."

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global gtime
    gtime += 1
    print int(gtime)
    
timer = simplegui.create_timer(100, timer_handler)


# define draw handler
def draw(canvas):
    canvas.draw_text(format(gtime), [100, 100], 24, "White")
    
# create frame
frame = simplegui.create_frame("Time in'", 200, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start Timer", start_timer, 200)
frame.add_button("Stop Timer", stop_timer, 200)
frame.add_button("Reset Timer", reset_timer, 200)
frame.add_input("Set Custom Time", set_custom_time, 200)

# start frame
new_game()

# Please remember to review the grading rubric
