# In the previous week's material we examined the format of images and created our own simplified bitmap viewer.

from tkinter import *

# standard dimensions for our window
WIDTH = 800
HEIGHT = 600

win = Tk()  # as before, creates a window
win.title('Image viewer!')

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# load the image
python_log_img = PhotoImage(file="python_logo.png")

# display the img, placing its center at the center of the canvas
canvas.create_image(WIDTH/2, HEIGHT/2, image=python_log_img)

win.mainloop()

# TODO Study this code, then solve Exercise0601
