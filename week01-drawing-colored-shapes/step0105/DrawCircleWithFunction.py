# In this exercise, we will create a window and draw a circle in it.
# But this time, we will define a function so we can easily draw a circle of any radius, at any point with ease.

# Let's start with importing the 'tkinter' library again.
from tkinter import *


# In Python, functions are declared using the 'def' keyword, followed by the name of the function, and then the
# parameters in brackets. The declaration ends with a colon ':' character.
# An important detail is that Python strictly enforces indentation. For instance, rather than using curly brackets,
# like Java, C/C++, etc. do, the body of the function is *implied* because the lines in the function are indented
# accordingly.
# This is an important characteristic: Python uses indentation to indicate a block of code. Improper indentation will
# lead to compile-time or runtime or logical errors.
# Finally, note that functions are supposed to be separated with exactly 2 empty lines before and after their
# declaration. Thankfully, the IDE is very useful in guiding us to conform to these specs.
# In the following function, the arguments are:
#   - c: the widget on which the circle is drawn.
#   - x: the horizontal coordinate (offset from left, in pixels) for the circle center.
#   - y: the vertical coordinate (offset from top, in pixels) for the circle center.
#   - radius: the circle radius, in pixels.
def draw_circle(c, x, y, radius):

    # Start by computing the 'top-left' and 'bottom-right' coordinates.
    x1 = x - radius  # circle center minus radius
    y1 = y - radius  # circle center plus radius
    x2 = x + radius  # circle center minus radius
    y2 = y + radius  # circle center plus radius

    # Then, draw the circle.
    c.create_oval(x1, y1, x2, y2)
    # This is the end of the function. Remember, 2 empty lines are expected before resuming with the rest of the code.


TITLE = 'Drawing a Circle with a Function'
WIDTH = 800
HEIGHT = 600

# Create the Window
win = Tk()
win.title(TITLE)
win.geometry(str(WIDTH)+'x'+str(HEIGHT))  # remember the argument must be a string such as '800x600'

# Create and pack the canvas.
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# Note how Python allows you to declare and initialize two (or more) variables at once, as follows:
c_x, c_y = 400, 300  # set the center of the circle at the center of the window, i.e. at WIDTH/2, HEIGHT/2

# In Python, you call a function using its name, followed by brackets.
# An important difference in Python is that the arguments can be named, and in this way can be specified in any order.
draw_circle(c=canvas, x=c_x, y=c_y, radius=50)

win.mainloop()  # Always, the last command must be the 'mainloop()' to run the GUI.
