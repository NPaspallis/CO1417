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
FRAMES_SUN = 4

# load the background images
sky_and_clouds_img = PhotoImage(file='background-sky-and-clouds.png')
trees_and_buildings_img = PhotoImage(file='background-trees-and-buildings.png')
ground_img = PhotoImage(file='background-ground.png')
pipes_img = PhotoImage(file='pipes.png')
sun_imgs = [PhotoImage(file='sun%i.png' % i) for i in range(FRAMES_SUN)]
# display the background images
sky_and_clouds_obj = canvas.create_image(WIDTH / 2, HEIGHT / 2, image=sky_and_clouds_img)
sun_obj = canvas.create_image(WIDTH - sun_imgs[0].width()/2, sun_imgs[0].height()/2, image=sun_imgs[0])
trees_and_buildings_obj = canvas.create_image(WIDTH / 2, HEIGHT - trees_and_buildings_img.height()/2 - ground_img.height(), image=trees_and_buildings_img)
ground_obj = canvas.create_image(WIDTH / 2, HEIGHT - ground_img.height() / 2, image=ground_img)
pipes_obj = canvas.create_image(WIDTH/2, HEIGHT-150, image=pipes_img)

animation_index = 0
sun_frame_index = 0


def update():
    """
    This function is called periodically to update the animation. It resets the background when it falls off the screen.
    """
    global animation_index, sun_frame_index

    # first handle the 'sky and clouds' part of the background - it moves at a slow pace
    (x,y) = canvas.coords(sky_and_clouds_obj)  # this picks the coordinates of the given object
    if x >= 0:
        canvas.move(sky_and_clouds_obj, -2, 0)  # move the background to the left by changing the X by an offset
    else:
        canvas.move(sky_and_clouds_obj, WIDTH, 0)  # reset the background, moving it back to the starting point

    # next handle the 'trees and buildings' part of the background - it moves at a medium pace
    (x,y) = canvas.coords(trees_and_buildings_obj)  # this picks the coordinates of the given object
    if x >= 0:
        canvas.move(trees_and_buildings_obj, -5, 0)  # move the background to the left by changing the X
    else:
        canvas.move(trees_and_buildings_obj, WIDTH, 0)  # reset the background, moving it back to the starting point

    # next handle the 'ground' part of the background - it moves at a faster pace
    (x,y) = canvas.coords(ground_obj)
    if x >= 0:
        canvas.move(ground_obj, -15, 0)  # move the background to the left by changing the X
    else:
        canvas.move(ground_obj, WIDTH, 0)  # reset the background, moving it back to the starting point

    # next handle the 'pipes' - it moves at the same pace as the 'ground'
    (x,y) = canvas.coords(pipes_obj)
    if x >= -pipes_img.width():
        canvas.move(pipes_obj, -15, 0)  # move the background to the left by changing the X
    else:
        canvas.move(pipes_obj, WIDTH+pipes_img.width(), 0)  # reset the background, moving it back to the starting point

    # finally, animate the sun
    canvas.itemconfig(sun_obj, image=sun_imgs[sun_frame_index])
    if animation_index % 10 == 0:
        sun_frame_index = sun_frame_index + 1
        if sun_frame_index >= FRAMES_SUN:
            sun_frame_index = 0

    animation_index = animation_index + 1

    win.after(DELAY, update)  # repeat the loop


win.after(0, update)
win.mainloop()
