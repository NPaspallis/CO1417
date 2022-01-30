# Enhancing the smiley.py program to draw a 'big' smile, where each pixel is actually 10x10.
from tkinter import *

# standard dimensions for our window
WIDTH = 800
HEIGHT = 640

win = Tk()  # as before, creates a window
win.title('Say big cheese!')

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

PIXEL_SIZE = 10 # now let's 'enlarge' or drawing by magnifying each 'pixel' by 10


# A simple method to draw a pixel in the window, at position (x,y), with the specified color
def draw_big_pixel(x, y, color):
    # note how the pixel is now a rectangle of size PIXEL_SIZE, starting at [x,y] (left, top) and reaching up to
    # [x+PIXEL_SIZE, y+PIXEL_SIZE] (right, bottom)
    canvas.create_rectangle(x, y, x+PIXEL_SIZE, y+PIXEL_SIZE, outline='', fill=color)


# same old smiley :-)
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


# Draws pixels that correspond to the given array with the given 'row_width'.
# Main difference compared to the previous step, is in computing the coordinates of the pixels to be drawn.
def draw_big_array(a, row_width, color, pos_x, pos_y):
    array_size = len(a)
    height = array_size // row_width
    for y in range(height):
        for x in range(row_width):
            if smiley[y*row_width+x]:
                # the top-left coordinates take into account that each pixel is PIXEL_SIZE wide and high
                draw_big_pixel(pos_x + x*PIXEL_SIZE, pos_y + y*PIXEL_SIZE, color)
            else:
                draw_big_pixel(pos_x + x*PIXEL_SIZE, pos_y + y*PIXEL_SIZE, 'white')


SMILE_SIZE = 8*PIXEL_SIZE
draw_big_array(smiley, 8, 'green', WIDTH/2-SMILE_SIZE/2, HEIGHT/2-SMILE_SIZE/2)

win.mainloop()  # listens for events, such as key presses and mouse clicks
