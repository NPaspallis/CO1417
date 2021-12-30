# This exercise continues the work of the previous one. It introduces a new feature where clicking the mouse changes
# the color used for fill in the drawn circles.
# The main goals of this exercise:
#   1. Familiarize with mouse click events.
#   2. Familiarize with Python Lists.

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

color = 'red'  # Set the circle fill color to 'gray'.
print('Move the mouse to draw circles!')  # Tell the user to move the mouse.
print('Click the mouse button to change color!')  # Tell the user to click the mouse button.


# This function simply handles the mouse motion events. The mouse coordinates are extracted from the 'event' argument.
# Then those coordinates (mouse_x, mouse_y) are used to center the new circle around it.
def move(event):
    mouse_x = event.x
    mouse_y = event.y
    canvas.create_oval(mouse_x-RADIUS, mouse_y-RADIUS, mouse_x+RADIUS, mouse_y+RADIUS, fill=color)


# This is where we bound the special event '<Motion>' which corresponds to the mouse movement, to the 'move' function
# specified above.
win.bind('<Motion>', move)

# All the code up to here is the same as in the previous exercise.
# Python has 4 main data structures built in the language: Lists, Tuples, Sets, and Dictionaries.
# The most common data structure is the List, which is essentially a sequence of values (of any type).
# The main characteristics of Lists are: they are ordered, they are editable, and the allow multiple copies of the same
# value. You can learn more at: https://www.w3schools.com/python/python_lists.asp.
# In this example, we define a new list containing a sequence of colors (as strings) to be used for switching the fill
# color of the drawn circle.
colors = ['red', 'blue', 'green', 'orange', 'cyan', 'yellow']  # Note how Lists use square brackets to initialize.
# Lists are zero-indexed, like arrays in Java/C/C++. This index points to the currently selected color.
selected_color_index = 0


# Next, define an appropriate function to swap the color. This is later linked to the mouse click action.
def change_color(event):
    # Since we access (and modify) the values 'color' and 'selected_color_index' from the outside scope, we need to
    # define those as 'global'. This allows the function to modify these values which were defined earlier.
    global color, selected_color_index
    selected_color_index = selected_color_index + 1  # Move the index to the next value ...
    if selected_color_index > len(colors) - 1:  # If the index moved past the last item ...
        selected_color_index = 0                # ... Then reset it to zero (first item)
    color = colors[selected_color_index]  # Finally, pick the indexed value as the next 'color'


win.bind('<Button-1>', change_color)  # Button-1 is the primary button (typically the left-click)

win.mainloop()  # listens for events, such as key presses and mouse clicks
