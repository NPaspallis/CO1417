# A simple program, drawing an image from an array.
from tkinter import *

# standard dimensions for our window
WIDTH = 800
HEIGHT = 600

win = Tk()  # as before, creates a window
win.title('Say cheese!')

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()


# A simple method to draw a pixel in the window, at position (x,y), with the specified color
def draw_pixel(x, y, color):
    canvas.create_rectangle(x, y, x, y, outline='', fill=color)


# let's create a smiley face! compare this array to 'smiley.png'
smiley = [
    False, False, False, False, False, False, False, False,
    False, True, True, False, False, True, True, False,
    False, True, True, False, False, True, True, False,
    False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False,
    False, True, False, False, False, False, True, False,
    False, False, True, True, True, True, False, False,
    False, False, False, False, False, False, False, False,
]


# Draws pixels that correspond to the given array with the given 'row_width'
def draw_array(a, row_width):
    # first, let's compute the size of the drawing
    # we already know the width is 'row_width' pixels
    # what is the height? pause a second and think before reading any further
    # ...
    # ...
    # ok the height must be 'array_size' / 'width' (because it is a rectangle!)
    array_size = len(a)
    height = array_size // row_width  # Quick question: why ise '//' instead of '/' for the division?
    for y in range(height):
        for x in range(row_width):
            if smiley[y*row_width+x]:
                draw_pixel(x, y, 'black')
            else:
                draw_pixel(x, y, 'white')


draw_array(smiley, 8)

win.mainloop()  # listens for events, such as key presses and mouse clicks

# To make it more interesting, improve the function 'draw_array' as follows:
# TODO First, add a third parameter 'color' to allow you to draw colored rather than black pixels. Try it out with your
#       favourite colors ('red', 'green', etc.). Call the resulting function 'draw_array2'.
# TODO Second, add two more parameters to specify where the top-left corner of the drawing should be. In its current
#       form, the 'draw_array' picture always draws the array starting at top-left (i.e., [0,0] position). Try it out
#       by calling the function to start at the center of the window, i.e., at [WIDTH//2, HEIGHT//2]. Call the resulting
#       function 'draw_array3'.
