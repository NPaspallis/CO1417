# This program continues with classes, a feature of object-Oriented Programming.

from tkinter import *
from random import randint  # the 'randint' is needed for generating random integers - used to position balls at random
# initial coordinates

WIDTH = 800
HEIGHT = 600
DELAY = 20  # delay between animations, in milliseconds

DEFAULT_SPEED = 5
DEFAULT_BALL_RADIUS = 10
DEFAULT_COLORS = ['red', 'green', 'blue', 'yellow', 'cyan', 'purple', 'orange', 'pink', 'white', 'black']

win = Tk()  # as before, creates a window
win.title('Simple animation over both axes, defining many balls moving randomly')


# Define a class named 'Ball'.
# This will provide a convenient method for collecting all the data for a Ball (such as its coordinates, speed, size,
# and color), as well as its functionality (such as moving and drawing it).
class Ball:

    def __init__(self, x, y, speed_x, speed_y, radius, color):
        self.x = x  # in Python, it's enough to declare a class value implicitly (in this case 'self.x' etc.)
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.color = color
        self.canvas_object = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=self.color, outline='black')

    def move(self):
        # first update the X...
        self.x = self.x + self.speed_x
        # ...then make sure that if it bounces, the horizontal speed is reversed
        if self.x >= WIDTH - self.radius:
            self.speed_x = -abs(self.speed_x)
        if self.x <= self.radius:
            self.speed_x = abs(self.speed_x)
        # next update the Y...
        self.y = self.y + self.speed_y
        # ...and make sure that if it bounces, the vertical speed is reversed
        if self.y >= HEIGHT - self.radius:
            self.speed_y = -abs(self.speed_y)
        if self.y <= self.radius:
            self.speed_y = abs(self.speed_y)

    def draw(self):
        canvas.coords(self.canvas_object, self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius)


canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

NUM_OF_BALLS = 20
balls = []
for r in range(1, NUM_OF_BALLS):
    b = Ball(
        randint(0,WIDTH-1), randint(0,HEIGHT-1),  # choose random coordinates within the window
        randint(-DEFAULT_SPEED,DEFAULT_SPEED), randint(-DEFAULT_SPEED,DEFAULT_SPEED),  # choose random speed in the range [-10,10] in either direction
        r,  # set radius to the chosen number in the range 1..20 - this ensures every ball has a different width
        DEFAULT_COLORS[randint(0, len(DEFAULT_COLORS)-1)])  # choose a random color from the DEFAULT_COLORS
    balls.append(b)


def animation():
    global balls
    for b_i in balls:
        b_i.move()
        b_i.draw()
    canvas.after(DELAY, animation)


# todo Modify the code so that when you click with the mouse in the window, a new ball of random radius/color appears.

animation()

win.mainloop()  # listens for events, such as key presses and mouse clicks
