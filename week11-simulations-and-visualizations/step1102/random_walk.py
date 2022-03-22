# random walk
import random
from tkinter import *

DIRECTIONS = ['up', 'right', 'down', 'left']


def random_direction() -> str:
    """Returns one of 'up', 'right', 'down', 'left' in random"""
    return 'up'


TITLE = 'Random Walk'
WIDTH = 800
HEIGHT = 800
RADIUS = 100

# Create the Window.
win = Tk()
win.title(TITLE)
win.geometry(str(WIDTH) + "x" + str(HEIGHT))

# Create and pack the canvas.
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

DELAY = 10
STEPS = 1000
current_round = 0
text_object = canvas.create_text(WIDTH-30, HEIGHT-20, text='0')
pos = (WIDTH/2, HEIGHT/2)


def update():
    """
    Implements one iteration of the 'random walk'.
    As a first step, a random direction is decided.
    Then, the new position is computed, and a path is drawn from the previous position, to the new one.
    Lastly, we check the position, and if it is outside the window we terminate the loop.
    """
    global pos, current_round
    current_round = current_round + 1
    canvas.itemconfig(text_object, text=str(current_round))
    (old_x, old_y) = pos
    direction = random_direction()
    if direction == 'up':
        pos = (pos[0], pos[1] - 10)
    if direction == 'down':
        pos = (pos[0], pos[1] + 10)
    if direction == 'left':
        pos = (pos[0] - 10, pos[1])
    if direction == 'right':
        pos = (pos[0] + 10, pos[1])
    (x, y) = pos
    canvas.create_line(old_x, old_y, x, y)
    if x < 0 or x > WIDTH or y < 0 or y > HEIGHT:  # when it goes outside the window, then quit
        print('Quiting at step:', current_round)
        return
    win.after(DELAY, update)


# draw indicative circles from center
canvas.create_oval(WIDTH / 2 - 2, HEIGHT / 2 - 2, WIDTH / 2 + 2, HEIGHT / 2 + 2, fill='red')  # small red dot in the center
for r in range(0, WIDTH + HEIGHT, 100):  # add red circles at radii 100, 200, 300, ...
    canvas.create_oval(WIDTH/2 - r/2, HEIGHT/2 - r/2, WIDTH/2 + r/2, HEIGHT/2 + r/2, outline='red')

win.after(0, update)  # start the simulation

win.bind('Q', quit)  # bind 'Q' to quit
win.bind('q', quit)  # bind 'q' to quit

win.mainloop()
