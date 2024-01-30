# This exercise introduces new functionality: It keeps track of the drawn circles, and deletes the oldest ones.
# To do so, we use a List to hold the IDs of the created circles, and utilize its 'pop' function to remove a specified
# value from it.
# The main goals of this exercise:
#   1. Familiarize with List and its 'append' and 'pop' functions.
#   2. Familiarize with the canvas 'delete' function.

# Let's start with importing the 'graphics' library again.
from tkinter import *

TITLE = 'Drawing many circles with the mouse'
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

# Note that we define a new List to hold the drawn circles. Initially it is empty (defines with '[]').
drawn_circles = []
MAX_SIZE = 20  # This is the max number of circles to keep on screen. Once we reach this limit, we delete the oldest.


# This function simply handles the mouse motion events. The mouse coordinates are extracted from the 'event' argument.
# Then those coordinates (mouse_x, mouse_y) are used to center the new circle around it.
def move(event):
    coordinates = (event.x, event.y)
    mouse_x = coordinates[0]  # As Tuples are ordered, their content can be accessed using an index in square brackets.
    mouse_y = coordinates[1]
    # A main difference compared to the previous exercise is that we take the ID of the created oval object ...
    circle_id = canvas.create_oval(mouse_x-RADIUS, mouse_y-RADIUS, mouse_x+RADIUS, mouse_y+RADIUS, fill=color)
    #  ... and save it by adding it to the end of a List using the 'append' function.
    drawn_circles.append(circle_id)
    # At this point we check whether our structure has exceeded its intended capacity: SIZE.
    if len(drawn_circles) > MAX_SIZE:
        # If we have more circles than SIZE then we need to delete the oldest one.
        # While we delete it, we also need to get its ID, so we can delete it from the canvas.
        id_of_circle_to_be_deleted = drawn_circles.pop(0)  # The 'pop' function removes and returns the specified
        # element from the List. To remove and return the first one, we specify its index, which is 0.
        # Then we use the 'delete' function of the Canvas, which takes an object id and deletes it.
        canvas.delete(id_of_circle_to_be_deleted)


win.bind('<Motion>', move)

win.mainloop()  # listens for events, such as key presses and mouse clicks
