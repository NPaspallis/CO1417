# Exercise 0104

The attached code is supposed to print a checker pattern (like a chessboard). But it has a bug.
You are asked to fix the bug.

Hint:
- The solution is as simple as adding just one line of code.

```python
# Let's start with importing the 'tkinter' library
from tkinter import *


# In this following function, the arguments are:
#   - c: the widget on which the square is drawn.
#   - c_x: the horizontal coordinate (offset from left, in pixels) for the square center.
#   - c_y: the vertical coordinate (offset from top, in pixels) for the square center.
#   - s: the square side, in pixels.
#   - col: color
def draw_square(c, s_x, s_y, s, col):

    # Start by computing the 'top-left' and 'bottom-right' coordinates.
    x1 = s_x - s/2  # square center minus side/2
    y1 = s_y - s/2  # square center plus side/2
    x2 = s_x + s/2  # square center minus side/2
    y2 = s_y + s/2  # square center plus side/2

    # Then, draw the square.
    c.create_rectangle(x1, y1, x2, y2, fill=col)
    # This is the end of the function. Remember, 2 empty lines are expected before resuming with the rest of the code.


TITLE = 'Drawing a Chessboard with Nested Loops - Where is the bug?'
WIDTH = 800
HEIGHT = 600

# Create the Window
win = Tk()
win.title(TITLE)
win.geometry(str(WIDTH)+'x'+str(HEIGHT))  # remember the argument must be a string such as '800x600'

# Create and pack the canvas.
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# Again, let the circle radius be 50.
side = 50
black = True

for x in range(side//2, WIDTH, side):  # The double slash ensures an integer division (i.e. not a floating number).
    for y in range(side//2, HEIGHT, side):
        print('Drawing a square at x=', x, ', y=', y)
        black = not black  
        if black:
            color = 'black'
        else:
            color = 'white'
        draw_square(canvas, x, y, side, color)

win.mainloop()  # Always, the last command must be the 'mainloop()' to run the GUI.

```

This is what the correct output should look like:
![checker board](https://raw.githubusercontent.com/NPaspallis/CO1417/main/week01-drawing-colored-shapes/xtras/Exercise0104.png)
