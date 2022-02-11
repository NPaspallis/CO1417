from tkinter import *

# standard dimensions for our window
WIDTH = 800
HEIGHT = 600

win = Tk()  # as before, creates a window
win.title('GIF viewer!')

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# define an empty list - we will use this to store the image frames in it
traffic_lights_frames = []

# load the individual frames
traffic_lights_frames.append(PhotoImage(file="frames/frame_0.gif"))  # loads the 1st image and inserts it at the end of the list
traffic_lights_frames.append(PhotoImage(file="frames/frame_1.gif"))  # loads the 2nd image and inserts it at the end of the list
traffic_lights_frames.append(PhotoImage(file="frames/frame_2.gif"))  # etc.
traffic_lights_frames.append(PhotoImage(file="frames/frame_3.gif"))  # etc.

# use a Label widget to display the images inside - you can learn more about Label and other TK widgets at
# https://www.dummies.com/article/technology/programming-web-design/python/using-tkinter-widgets-in-python-141443
label = Label(canvas)
# display the Label (containing the image) at the center of the canvas
canvas.create_window(WIDTH/2, HEIGHT/2, window=label)

# define constants
DELAY = 1000  # the delay between each frame - 1000 ms = 1 sec


# The update function is used to drive the animation.
# In each iteration, this function draws the current frame, and moves the index to point to the next frame
def update(index):
    frame = traffic_lights_frames[index]  # index - initial values is 0 by default
    label.configure(image=frame)  # set the current frame as the image displayed in the label
    index += 1  # point index to the next frame
    if index == len(traffic_lights_frames):  # when you go beyond the list size, point back to the first frame (index 0)
        index = 0
    win.after(DELAY, update, index)  # wait DELAY ms and then loop to form the animation


win.after(0, update, 0)
win.mainloop()

# TODO Work on Exercise0602
