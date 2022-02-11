# Image Viewer

In this simple example we demonstrate how to load an image from a file, and then display it
on top of the canvas.

Here is the full code:

```python
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
```

And here is the resulting screenshot:

![Python Logo](image_viewer_screenshot.png)
