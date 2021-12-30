# In this exercise, we will create a window and draw circles in it.
# This time, we catch the mouse movement and draw circles at the cursor position.

# Let's start with importing the 'graphics' library again.
from tkinter import *

TITLE = 'Drawing circles with the mouse'
WIDTH = 800
HEIGHT = 600
RADIUS = 100

# Create the Window.
win = Tk()
win.title(TITLE)
win.geometry(str(WIDTH) + "x" + str(HEIGHT))

# Create and pack the canvas.
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

color = 'red'  # Set the circle fill color to 'red'.
print('Move the mouse to draw circles!')  # Tell the user to move the mouse.


# This function simply handles the mouse motion events. The mouse coordinates are extracted from the 'event' argument.
# Then, those coordinates (mouse_x, mouse_y) are used to center the new circle at the mouse pointer.
def move(event):
    mouse_x = event.x
    mouse_y = event.y
    canvas.create_oval(mouse_x-RADIUS, mouse_y-RADIUS, mouse_x+RADIUS, mouse_y+RADIUS, fill=color)


# This is where we bound the special event '<Motion>' which corresponds to the mouse movement, to the 'move' function
# specified above.
win.bind('<Motion>', move)

win.mainloop()  # listens for events, such as key presses and mouse clicks
