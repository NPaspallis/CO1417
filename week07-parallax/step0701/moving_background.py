from tkinter import *

# standard dimensions for our window
WIDTH = 800
HEIGHT = 600

win = Tk()  # as before, creates a window
win.title('Moving background')

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
    This function is called periodically to update the animation
    """
    (x,y) = canvas.coords(background_obj)  # this picks the coordinates of the given object
    print("x: ", x)  # print the X coordinates of the object
    canvas.move(background_obj, -20, 0)  # move the background to the left by changing the X by -20
    win.after(DELAY, update)  # repeat the loop


win.after(0, update)
win.mainloop()

# TODO Solve Exercise0701
