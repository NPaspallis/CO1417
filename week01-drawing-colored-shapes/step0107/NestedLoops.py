# In this exercise, we will familiarize with nesting of loops in Python. For this, we will use a window and draw circles
# in multiple rows. Like before, we will use a function to ease the task of drawing circles.

# Let's start with importing the 'tkinter' library again.
from tkinter import *


# Reuse the same function from the previous step.
# In this following function, the arguments are:
#   - c: the widget on which the circle is drawn.
#   - c_x: the horizontal coordinate (offset from left, in pixels) for the circle center.
#   - c_y: the vertical coordinate (offset from top, in pixels) for the circle center.
#   - r: the circle radius, in pixels.
def draw_circle(c, c_x, c_y, r):

    # Start by computing the 'top-left' and 'bottom-right' coordinates.
    x1 = c_x - r  # circle center minus radius
    y1 = c_y - r  # circle center plus radius
    x2 = c_x + r  # circle center minus radius
    y2 = c_y + r  # circle center plus radius

    # Then, draw the circle.
    c.create_oval(x1, y1, x2, y2)
    # This is the end of the function. Remember, 2 empty lines are expected before resuming with the rest of the code.


TITLE = 'Drawing Circles with Nested Loops'
WIDTH = 800
HEIGHT = 600

# Create the Window
win = Tk()
win.title(TITLE)
win.geometry(str(WIDTH)+'x'+str(HEIGHT))  # remember the argument must be a string such as '800x600'

# Create and pack the canvas.
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()


# Let's aim to draw many adjacent circles of radius 50. For this, we need to assign (x,y) -- the circle center -- all
# the values from left to right, and from top to bottom, spaced at 2 x radius.
# In Python, there is a handy 'for-range' statement where you can easily assign values like that.

# Again, let the circle radius be 50.
radius = 50

for x in range(radius, WIDTH, 2 * radius):
    for y in range(radius, HEIGHT, 2 * radius):
        print('Drawing a circle at x=', x, ', y=', y)
        draw_circle(canvas, x, y, radius)

win.mainloop()  # Always, the last command must be the 'mainloop()' to run the GUI.
