# In this exercise, we extend the program from the previous one.
# We will define a function to handle arbitrary key presses to change the color of the drawn circle.

# Let's start with importing the 'tkinter' library again.
from tkinter import *

TITLE = 'Handling keyboard input to draw colored circles'
WIDTH = 800
HEIGHT = 600

# Create the Window.
win = Tk()
win.title(TITLE)
win.geometry(str(WIDTH) + "x" + str(HEIGHT))

# Use 'x' and 'y' to be the circle center. Initialize them to be at the center of the window.
x = WIDTH / 2
y = HEIGHT / 2
# Circle radius and color.
radius = 100
color = 'gray'  # Todo Note the additional value 'color'. This is used when we draw a circle to define its fill.

# Create and pack the canvas.
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# Draw the circle at (x,y).
canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)  # draw the circle
print('Use the arrow keys to draw the circle elsewhere in the window!')
print('Press X to exit.')


# As before: The 'left' function handles the left arrow key, etc.
# In addition, compared to the previous program, the circles are colored by setting their 'fill'.
def left(event):
    global x  # The 'global keyword here means: Do not define a new value. Reuse the existing one from the outer scope.
    x = x - 10  # Move the circle 10 pixels to the left.
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)


def right(event):
    global x
    x = x + 10  # Move the circle 10 pixels to the right.
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)


def up(event):
    global y
    y = y - 10  # Move the circle 10 pixels up.
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)


def down(event):
    global y
    y = y + 10  # Move the circle 10 pixels down.
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)


# This function is called to handle arbitrary key presses.
# At the moment, it detects when you press 'x', in which case it quits.
# Todo: Modify this function so that when you press 'r' it changes the color to 'red', 'g' to 'green', 'b' to 'blue'.
def on_key_press(event):
    global color
    print('You pressed: ', event.char)
    if event.char == 'x' or event.char == 'X':  # handle small or capital X
        print("Bye!")
        quit()


win.bind('<Left>', left)
win.bind('<Right>', right)
win.bind('<Up>', up)
win.bind('<Down>', down)
# Note that the special code '<KeyPress>' is used to handle any key. See the output printed by the 'on_key_press'
# function.
win.bind('<KeyPress>', on_key_press)

win.mainloop()  # Always, the last command must be the 'mainloop()' to run the GUI.
