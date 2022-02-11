from tkinter import *

# standard dimensions for our window
WIDTH = 800
HEIGHT = 600

win = Tk()  # as before, creates a window
win.title('Welcome to your bitmap viewer!')

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

PIXEL_SIZE = 10  # assume each pixel is size 10
PICTURE_WIDTH = WIDTH // PIXEL_SIZE  # this is the # of 'pixels' on the horizontal dimension of the picture
PICTURE_HEIGHT = HEIGHT // PIXEL_SIZE  # this is the # of 'pixels' on the vertical dimension of the picture
picture = [False] * PICTURE_WIDTH * PICTURE_HEIGHT  # this is the array to store the image - initially it's all empty (white)


# A simple method to draw a pixel in the window, at position (x,y), with the specified color
def draw_big_pixel(x, y, color):
    canvas.create_rectangle(x, y, x+PIXEL_SIZE, y+PIXEL_SIZE, outline='', fill=color)


# Draws a grid to visualize the big pixel positions
def draw_grid():
    for x in range(0, WIDTH, PIXEL_SIZE):
        # draw vertical lines
        canvas.create_line(x, 0, x, HEIGHT, fill='gray')
    for y in range(0, WIDTH, PIXEL_SIZE):
        # draw horizontal lines
        canvas.create_line(0, y, WIDTH, y, fill='gray')


def draw_picture(p, row_width, color):
    for x in range(PICTURE_WIDTH):
        for y in range(PICTURE_HEIGHT):
            # draw the big 'pixels'
            if p[y*row_width+x]:  # checks the value of the pixel in the array
                c = color
            else:
                c = 'white'
            draw_big_pixel(x*PIXEL_SIZE, y*PIXEL_SIZE, c)


draw_picture(picture, PICTURE_WIDTH, 'black')
draw_grid()

win.mainloop()  # listens for events, such as key presses and mouse clicks

# Challenges:
# - TODO Add a mouse listener so that when you click anywhere on the window, you 'randomize' the contents of the
#       picture. By 'randomize' we mean, you set the value of each pixel in the 'picture' to True or False, randomly.
#       For an example, see a screenshot of how this could look in the "noise.png" picture.
#       For clarity, add the code that randomizes the content in a function called "add_noise".
#       This should be reflected in the drawn picture too (you should call 'draw_picture' and 'draw_grid' after each
#       event). If you need a refresh on how to handle mouse events, refer to step 0204 from week 2.

