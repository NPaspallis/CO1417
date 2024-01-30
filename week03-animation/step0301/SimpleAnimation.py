# This program demonstrates how to realize simple animations in a graphical application

from tkinter import *

WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 10
DELAY = 20  # delay between animations, in milliseconds

win = Tk()  # as before, creates a window
win.title('Simple animation')

# ball data
ball_x = WIDTH/2
ball_y = HEIGHT/2
ball_r = BALL_RADIUS
# the ball_speed_x determines the rate by which the X coordinate of the ball changes
ball_speed_x = 5

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# The 'canvas.create_oval' function returns the ID of the created object. We will reuse this later to update its
# coordinates.
ball_id = canvas.create_oval(ball_x - ball_r, ball_y - ball_r, ball_x + ball_r, ball_y + ball_r, fill='red', outline='black')


# This function implements the animation. Note how the last statement is calling itself again.
def animation():
    # When we need to have 'write' access to the values declared outside the function (i.e. globals), we need to
    # explicitly indicate that by using the 'global' keyword, as below.
    global ball_x, ball_y, ball_speed_x
    # The following line simply updates the X coordinate of the ball, increasing it a bit in each frame.
    ball_x += ball_speed_x

    # todo 1. Experiment by modifying the value of the 'ball_speed_x' (at line 18). Try smaller and larger values. Also
    #   try negatives.
    # todo 2. Edit the code so that the ball bounces back when it hits the right/left boundaries of the window.

    # The following call updates the coordinates of the ball with the ID 'ball_id', declared earlier.
    canvas.coords(ball_id, ball_x-ball_r, ball_y-ball_r, ball_x+ball_r, ball_y+ball_r)
    canvas.after(DELAY, animation)  # This calls this function (named 'animation') again, after waiting 'DELAY'
    # milliseconds.


animation()

win.mainloop()  # listens for events, such as key presses and mouse clicks
