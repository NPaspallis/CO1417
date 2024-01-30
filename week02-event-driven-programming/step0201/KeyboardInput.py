# In this exercise, we will create a window and draw a circle in it.
# But this time, we will define a function, so we can easily draw any circle at any point with any side size.
# Then we will handle input (in terms of key presses) to redraw the circle left/right/up/down respectively.

# Let's start with importing the 'tkinter' library again.
from tkinter import *

TITLE = 'Handling keyboard input to draw circles'
WIDTH = 800
HEIGHT = 600

# Create the Window.
win = Tk()
win.title(TITLE)
win.geometry(str(WIDTH) + "x" + str(HEIGHT))

# Use 'x' and 'y' to be the circle center. Initialize them to be at the center of the window.
x = WIDTH / 2
y = HEIGHT / 2
# Circle radius and color.
radius = 100

# Create and pack the canvas.
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# Draw the circle at (x,y).
canvas.create_oval(x-radius, y-radius, x+radius, y+radius)  # draw the circle
print('Use the arrow keys to draw the circle elsewhere in the window!')


# In the following, we define functions to handle the events of pressing the arrow keys on the keyboard.
# The 'left' function handles the left arrow key, etc.
# Each of these functions takes an argument 'event' which is required but not used.
def left(event):
    global x  # The 'global' keyword here means: Do not define a new value. Reuse the existing one from the outer scope.
    x = x - 10  # Move the circle 10 pixels to the left.
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius)  # draw the circle


def right(event):
    global x
    x = x + 10  # Move the circle 10 pixels to the right.
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius)  # draw the circle


def up(event):
    global y
    y = y - 10  # Move the circle 10 pixels up.
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius)  # draw the circle


def down(event):
    global y
    y = y + 10  # Move the circle 10 pixels down.
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius)  # draw the circle


# Now, bind the corresponding events (i.e. arrow key presses) to a named function.
# The functions must be defined 'before' they can be mentioned. That is why we define the functions first, then bind
# them to the corresponding key-press events.
win.bind('<Left>', left)  # Note how the 'left' arrow key is encoded as '<Left>'. Similarly, for the other arrow keys.
win.bind('<Right>', right) # The second argument of the 'bind' is the function to be called
win.bind('<Up>', up)
win.bind('<Down>', down)

win.mainloop()  # Always, the last command must be the 'mainloop()' to run the GUI.
