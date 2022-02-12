from tkinter import *

# standard dimensions for our window
WIDTH = 800
HEIGHT = 600

win = Tk()  # as before, creates a window
win.title('Moving background in loops')

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# define constants
DELAY = 100  # 100 ms = 0.1 sec

# load the background image
background_img = PhotoImage(file='background.png')
# display the background img at the center of the canvas
background_obj = canvas.create_image(WIDTH/2, HEIGHT/2, image=background_img)


def update():
    """
    This function is called periodically to update the animation. It resets the background when it falls off the screen.
    """
    (x,y) = canvas.coords(background_obj)  # this picks the coordinates of the given object
    print(x)
    if x >= -WIDTH/2:
        canvas.move(background_obj, -20, 0)  # move the background to the left by changing the X by -20
    else:
        print('reset')
        canvas.move(background_obj, WIDTH, 0)  # reset the background, moving it back to the starting point
    win.after(DELAY, update)  # repeat the loop


win.after(0, update)
win.mainloop()

# When the background image falls off the screen, you can reset its position and restart the animation.
# The problem is that half of the screen is empty. How can we solve this?
#
# A typical solution is to use a 'longer' image, e.g., one which is twice the screen width. But no matter how long the
# image, it will always be finite, and thus we need to reposition it.
#
# TODO Solve Exercise0702
