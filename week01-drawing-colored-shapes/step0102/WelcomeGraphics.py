# In CO1417 we will be using a lot of graphics -- i.e. drawing on a window, rather than just printing on the console
# We will be using Python's interface to Tcl/Tk, known as 'tkinter'.
# You can learn more about the tkinter library at: https://docs.python.org/3/library/tkinter.html.
#
# A software library is a collection of code (usually exposed as routines or data structures or classes) which provide
# some commonly used functionality.
# Rather than copy pasting the code in your own source files every time you want to use it, a library can be 'imported'
# using the 'import ...' and 'from ... import ...' statements.

# Ok, it's time to get started with drawing :-)
# First things first, we need to import the 'tkinter' library. This library includes multiple modules. For simplicity,
# we specify '*' to import everything.

from tkinter import *

# todo Verify that the above 'import' is not underlined in red. If it does not work, you might be missing the library
#   in your installation. In this case you can install it -- simply search online for 'install tkinter'.

# Ok, now we are ready to code our first graphics based app
# Note in the following line of code:
#   1. The 'win = Tk()' creates a simple graphical window.
#   2. The next line ('title') specifies the title for the window. Note how Python uses either "double quotes" or
#       'single quotes' to enclose a string.
#   3. The next line ('geometry') defines the dimensions of the window in pixels (width and height).
win = Tk()  # creates a GUI window (using the tkinter library)
win.title('Hello World!')  # sets window's title to 'Hello World!' (shown in the top area)
win.geometry('320x240')  # sets window's geometry to width: 320 pixels, height: 240 pixels


# When you run the above code, it does create and show a window. But since the programme terminates immediately
# afterwards, the window is disposed and taken off the screen before it can be examined.

# To keep the window around, we add the 'win.mainloop()' call which activates the window.
# todo Uncomment the following line and execute the program again.
# win.mainloop()  # listens for events, such as key presses and mouse clicks

# So this is all you need to know for creating a simple application which includes a graphics window!
# todo Try to modify the title of the window. Run the program again and verify it has indeed changed.
# todo Try to modify the dimensions of the window (e.g. double them). Run the program again and verify it has indeed
#   changed.
