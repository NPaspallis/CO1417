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

# load the background images
sky_and_clouds_img = PhotoImage(file='background-sky-and-clouds.png')
ground_img = PhotoImage(file='background-ground.png')
sun_img = PhotoImage(file='sun.png')  # a static image for decoration purposes
# display the background images
sky_and_clouds_obj = canvas.create_image(WIDTH / 2, HEIGHT / 2, image=sky_and_clouds_img)
ground_obj = canvas.create_image(WIDTH / 2, HEIGHT - ground_img.height() / 2, image=ground_img)
sun_obj = canvas.create_image(WIDTH - sun_img.width()/2, sun_img.height()/2, image=sun_img)


def update():
    """
    This function is called periodically to update the animation. It resets the background when it falls off the screen.
    """
    # first handle the 'sky and clouds' part of the background - it moves at a slow pace: 5 pixels / frame
    (x,y) = canvas.coords(sky_and_clouds_obj)  # this picks the coordinates of the given object
    if x >= 0:
        canvas.move(sky_and_clouds_obj, -5, 0)  # move the background to the left by changing the X by -20
        print(x)
    else:
        canvas.move(sky_and_clouds_obj, WIDTH, 0)  # reset the background, moving it back to the starting point
        print('reset ', x)

    # next handle the 'ground' part of the background - it moves at a faster pace: 20 pixels / frame
    (x,y) = canvas.coords(ground_obj)
    if x >= 0:
        canvas.move(ground_obj, -20, 0)  # move the background to the left by changing the X by -20
    else:
        canvas.move(ground_obj, WIDTH+40, 0)  # reset the background, moving it back to the starting point

    win.after(DELAY, update)  # repeat the loop


win.after(0, update)
win.mainloop()

# When the background image falls off the screen, you can reset its position and restart the animation.
# The problem is that half of the screen is empty. How can we solve this?
#
# A typical solution is to use a 'longer' image, e.g., one which is twice the screen width. But no matter how long the
# image, it will always be finite, and thus we need to reposition it.
#
# TODO Solve Exercise0703
