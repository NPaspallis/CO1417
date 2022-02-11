# In the previous week's material we examined the format of images and created our own simplified bitmap viewer.

from tkinter import *

# standard dimensions for our window
WIDTH = 800
HEIGHT = 600

win = Tk()  # as before, creates a window
win.title('Flappy wings!')

canvas = Canvas(win, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()

# define constants
DELAY = 100  # 100 ms = 0.1 sec
FRAME_COUNT = 9  # total # of frames in the animation

# load the individual frames - note this Python-specific trick: we add to the 'frames' array all PhotoImage objects
# acquired by iterating i in the range [0..FRAME_COUNT-1] (the '%i' part in the filename takes the values of i in the
# given range) - by the end of this statement, the 'frames' array contains the 9 image frames
frames = [PhotoImage(file='frames/frame_%i_delay-0.1s.gif' % i) for i in range(FRAME_COUNT)]

# display the img at the center of the canvas
flappy_wings = canvas.create_image(WIDTH/2, HEIGHT/2, image=frames[0])

# display a caption at the center-bottom of the window
caption_label = Label(canvas, text='frame')
canvas.create_window(WIDTH/2, HEIGHT-20, window=caption_label)

# the index of the current frame - used to drive the animation
frame_index = 0


def update():
    global frame_index # use global variable (defined outside the function)
    canvas.itemconfig(flappy_wings, image=frames[frame_index])
    caption_label.configure(text='frame %i' % frame_index)
    frame_index += 1
    if frame_index == FRAME_COUNT:
        frame_index = 0
    win.after(DELAY, update)


win.after(0, update)
win.mainloop()
