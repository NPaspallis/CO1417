# In this exercise, we will familiarize with loops in Python. For this, we will use a window and draw multiple circles
# in it. Like before, we will use a function to ease the task of drawing circles.

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


TITLE = 'Drawing Circles with a Loop'
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

# First, let the circle radius be 50.
radius = 50

# The for loop visits each value in a given 'range'.
# The range can be defined explicitly using the square brackets notation, as shown below:
my_range = [100, 200, 300, 400, 500, 600, 700]
# Then, each value in the 'range' can be visited using the 'for' statement. Also see below:
for x in my_range:
    print('Drawing a circle at x=', x)
    draw_circle(canvas, x, 100, radius)  # draws a circle at (x,100)

# Alternatively, you can use the 'range' function to produce the values programmatically. For example, the following
# produces a range from 0, until less than WIDTH, with a gap of '2 * radius' between them, i.e. [0, 100, ...700].
for x in range(0, WIDTH, 2 * radius):
    print('Drawing a circle at x=', x)
    draw_circle(canvas, x, 300, radius)

# todo You can learn more about the 'for' statement and the 'range' function at:
#   https://www.w3schools.com/python/python_for_loops.asp, and
#   https://www.w3schools.com/python/ref_func_range.asp, respectively.

# Finally, you can achieve a similar result using the 'while' statement to create a loop.
x = 100
while x < WIDTH:
    print('Drawing a circle at x=', x)
    draw_circle(canvas, x, 500, radius)
    x += 2 * radius

# todo You can learn more about the 'while' statement in Python at:
#   https://www.w3schools.com/python/python_while_loops.asp.

win.mainloop()  # Always, the last command must be the 'mainloop()' to run the GUI.
