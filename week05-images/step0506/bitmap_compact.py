from tkinter import *

# standard dimensions for our window -- matches the size of the bitmap to be displayed
WIDTH = 800
HEIGHT = 600

win = Tk()  # as before, creates a window
win.title('View a compact bitmap read from a file')

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()


# A simple method to draw a single pixel in the window, at position (x,y), with the specified color
def draw_pixel(x, y, color):
    canvas.create_rectangle(x, y, x, y, outline='', fill=color)


# This function draws the given bitmap with the given color.
# The bitmap_array_2d is a 2-Dimensional array: It contains a number of arrays corresponding to 'rows' in the bitmap.
# Each sub-array contains the values for the corresponding row, as a number of Boolean values.
# If the corresponding value is 'True', then it draws the 'foreground_color', else the 'background_color'.
# The first step is to compute the dimensions of the given bitmap.
# Then it uses two nested loops to scan each value of the 2-Dimensional array, processing row-by-row (from top to
# bottom) and for each row processing each pixel (from left to right)
def draw_bitmap(bitmap_array_2d, foreground_color, background_color):
    picture_width = len(bitmap_array_2d[0]) # compute picture width = length of first row
    picture_height = len(bitmap_array_2d) # compute picture height = number of rows
    for x in range(picture_width):
        for y in range(picture_height):
            if bitmap_array_2d[y][x]:  # checks the value of the pixel in the array
                c = foreground_color
            else:
                c = background_color
            draw_pixel(x, y, c)


# So far the code is very similar to what was presented earlier.
# The novelty is right here: we load a 2-Dimensional array from a file, by reading the T/F values from the
# 'universum-compact.txt' file.
# Have a look at the file universum-compact.txt'. You will notice it has a large number of text values of 'T' and 'F'.
# The first line contains a number which corresponds to the 'width' of the bitmap.
# The second line contains a number which corresponds to the 'height' of the bitmap.
# The remaining of the file contains 'height'-many lines, where each line contains 'width-many' values of 'T' or 'F'.
# The function first loads the width and height by reading (and consuming) the first two lines.
# Note: The use of function 'pop(0)' pops the first value. Pop(0) means read the first value (at index 0) and remove it.
# The remaining of the function reads the file line by line and inserts the read values in a 2-Dimensional Boolean
# array. The array (b) is first initialized with 'picture_height' empty arrays.
def load_bitmap(file_name):
    text_file = open(file_name, "r")  # opens the file for "read" operations
    lines = text_file.readlines()
    picture_width = int(lines.pop(0))  # first line is width
    picture_height = int(lines.pop(0))  # second line is height
    print("picture_width:  {}".format(picture_width))
    print("picture_height: {}".format(picture_height))
    y = 0  # init rows index
    b = [[]] * picture_height  # Init the array with 'height-many' empty arrays
    for line in lines:
        b[y] = [False] * picture_width  # Init each row with 'width-many' copies of False - i.e., the default value
        # the 'list' function (available in Python 3) takes as input a string and returns a list of the characters in that string
        # the strip() function clears the 'line' of any leading ot trailing whitespaces, such as <Enter>, etc.
        chars = list(line.strip())
        x = 0
        for char in chars:
            if char.strip() == 'T':
                b[y][x] = True  # Init only 'T' values - everything else is already 'False'
            x = x+1
        y = y+1

    text_file.close()  # closes the file (good practice)
    return b


bitmap_picture = load_bitmap("universum-compact.txt")
draw_bitmap(bitmap_picture, 'grey', 'white')

win.mainloop()  # listens for events, such as key presses and mouse clicks

# TODO Study and run the code in this program. The only changes compared to the `bitmap.py` of `step0505` concerns the
#       function `load_bitmap`. This function was adapted so it could read the 'compact' format of the file.
#       In `Exercise0504` you are asked to develop a new program which reads the more efficient, Hex-based format.
