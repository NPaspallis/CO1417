# In this exercise, we will create a window and draw a circle in it.

# Let's start with importing the 'tkinter' library again.
from tkinter import *  # note the use of '*' which means 'everything'

TITLE = 'Drawing a Circle'  # Remember, you can define strings using 'single quotes' or "double quotes" -- both are ok.
WIDTH = 800
HEIGHT = 600

# Create the Window
win = Tk()
win.title('Drawing a circle!')
win.geometry(str(WIDTH)+'x'+str(HEIGHT))  # remember the argument must be a string such as '800x600'

# todo Now, to the main goal of this exercise: Draw a circle.
#   1. So far we've created a window (the 'win' value). This can be used to add buttons, text, and other widgets. In
#       this case, we want to draw shapes, so the most appropriate widget is the 'Canvas' which allows to draw arbitrary
#       lines and shapes.
#       Note: The canvas object allows access to its 2D area in terms of coordinates. The top-left corner is the point
#       (0,0) and the bottom-right point is the (w,h) where 'w' is the canvas width and 'h' its height.

# Link the canvas to the 'win' and set its size (in this case the full window).
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
# The following command ('pack') packs the widget within the host window.
canvas.pack()

# todo
#   2. The tkinter library does not have a direct command to create a circle. But it has the more general command
#       'create_oval' which can be used to draw an arbitrary oval (remember that a circle is an oval where the width
#       and height are identical).
#       The command takes the following arguments: 'create_oval(x0,y0,x1,y1)', where the (x0,y0) and (x1,y1) points
#       are the top-left and bottom-right bounds of the oval -- see:
#       https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_oval.html.
#       For example, to create an oval that spans the whole canvas, simply use the (0,0) and (WIDTH,HEIGHT) coordinates.
#       You can try this out by uncommenting the following line:
# canvas.create_oval(0,0,WIDTH,HEIGHT)

# todo
#   3. Finally, draw a circle of radius '100' pixels at the center of the window.
radius = 100  # The circle radius (in pixels).
# The window center is at (WIDTH/2, HEIGHT/2).
# Thus the top-left bound of the circle must be 1/2 radius over and to the left: (WIDTH/2-radius/2, HEIGHT/2-radius/2)
# Similarly, the bottom-right bound must be 1/2 radius down and to the right: (WIDTH/2+radius/2, HEIGHT/2+radius/2)

# todo Uncomment the following line to draw the circle.
# canvas.create_oval(WIDTH/2-radius/2, HEIGHT/2-radius/2, WIDTH/2+radius/2, HEIGHT/2+radius/2)

# You can set the background color of the canvas using the 'bg' property.
# todo Uncomment the following line to set the canvas background color to 'green'.
# canvas.config(bg='green')

# The value can be any of the main colors (such as 'black', 'white', 'red', 'blue', 'green', 'yellow', etc.)
# For a complete list of the colors 'recognizable' by tkinter, see:
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter.
# todo Modify the program to set the canvas background to your favorite color.

win.mainloop()  # Always, the last command must be the 'mainloop()' to run the GUI.
