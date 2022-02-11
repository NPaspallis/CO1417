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

in_a_jump = False  # this boolean values tells us when already in a jump as to not start another one
# below are the movements of a jump over time - they must add up to 0 - having this instead of a fixed set of constant
# offsets (e.g., -10, -10, -10...) allows us to imitate a more natural jump (negative is up, positive is down)
jump_offsets = [0, -60, -45, -30, -20, 0, 20, 30, 45, 50, 25, -15, ]
# the jump index is used to keep track of the phase of the jump, it completes after len(jump_offsets) steps
jump_index = 0


# This function is called periodically to update the animation
def update():
    global frame_index, in_a_jump, jump_index  # use global variables (defined outside the function)
    canvas.itemconfig(flappy_wings, image=frames[frame_index])  # set the next frame to the 'flappy_wings' image

    # handle the 'jump' part of the animation
    if in_a_jump: # if in a jump, move the character by jump_offset
        jump_offset = jump_offsets[jump_index]  # pick the current offset
        canvas.move(flappy_wings, 0, jump_offset)  # the 'canvas.move' function moves the specified object by the given X,Y pixels
        jump_index = jump_index + 1  # prepare for the next phase of the jump
        if jump_index > len(jump_offsets)-1:  # when the jump ends...
            jump_index = 0  # ...reset the jump_index...
            in_a_jump = False  # ...and set in_a_jump back to False

    # update the frame picture
    caption_label.configure(text='frame %i' % frame_index)
    frame_index += 1
    if frame_index == FRAME_COUNT:
        frame_index = 0
    win.after(DELAY, update)


# This function is called when a jump is initiated
def jump(__self__):
    global in_a_jump  # use global variable (defined outside the function)
    if not in_a_jump:  # only process the jump event if no other jump is in progress
        in_a_jump = True


win.bind("<space>", jump)

win.after(0, update)
win.mainloop()

# TODO Solve Exercise0603.
