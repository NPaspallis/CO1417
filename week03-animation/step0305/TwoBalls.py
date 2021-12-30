# This program introduces classes, a feature of object-Oriented Programming.
# At its core, Object-Oriented Programming (OOP) organizes programs into main concepts (classes) which define code
# for abstracting data (values) and behavior (functions).
# In this example we demonstrate OOP with a Ball class. This class concentrates all necessary data for a Ball: The
# data includes the position of the ball (x,y), its speed (speed_x,speed_y), its width, color, etc. The functionality
# includes the ability of the ball to update its position based on its speed, and to cycle its colour.
#
# This page provides a good introduction to Object-Oriented Programming with Python:
# https://www.w3schools.com/python/python_classes.asp

from tkinter import *
from random import randint  # the 'randint' is needed for generating random integers - used to position balls at random initial coordinates

WIDTH = 800
HEIGHT = 600
DELAY = 20  # delay between animations, in milliseconds

DEFAULT_SPEED = 5
DEFAULT_BALL_RADIUS = 10
DEFAULT_COLORS = ['red', 'green', 'blue', 'yellow', 'cyan']

win = Tk()  # as before, creates a window
win.title('Simple animation over both axes, defining two balls as objects')


# Define a class named 'Ball'.
# This will provide a convenient method for collecting all the data for a Ball (such as its coordinates, speed, size,
# and color), as well as its functionality (such as moving and drawing it).
class Ball:

    # The __init__ is a special function called 'constructor'. It is used to initialize the
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

# randint(x,y) generates a random integer in the range  [x,y] (inclusive)
b1 = Ball(
    randint(0,WIDTH-1), randint(0,HEIGHT-1),  # choose random coordinates within the window
    randint(-DEFAULT_SPEED,DEFAULT_SPEED), randint(-DEFAULT_SPEED,DEFAULT_SPEED),  # choose random speed in the range [-10,10] in either direction
    randint(DEFAULT_BALL_RADIUS-5, DEFAULT_BALL_RADIUS+5),  # choose a random ball radius in the range [5,15]
    DEFAULT_COLORS[randint(0, len(DEFAULT_COLORS)-1)])  # choose a random color from the DEFAULT_COLORS
b2 = Ball(
    randint(0,WIDTH-1), randint(0,HEIGHT-1),
    randint(-DEFAULT_SPEED,DEFAULT_SPEED), randint(-DEFAULT_SPEED,DEFAULT_SPEED),
    randint(DEFAULT_BALL_RADIUS-5, DEFAULT_BALL_RADIUS+5),
    DEFAULT_COLORS[randint(0, len(DEFAULT_COLORS)-1)])


def animation():
    global b1, b2
    b1.move()
    b2.move()
    b1.draw()
    b2.draw()
    canvas.after(DELAY, animation)


# todo Modify the code so that it generates multiple balls, e.g., 20 - aim to use a for-loop rather than copy-paste the code
animation()

win.mainloop()  # listens for events, such as key presses and mouse clicks
