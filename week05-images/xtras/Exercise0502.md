# Exercise 0502 - Random Noise

Starting from the code of [image_viewer.py](../step0503/bitmap_viewer.py) in step 0503, we will add a mouse listener to
*randomize* the pixels on each click.

Your goal is to add a mouse listener so that when you click anywhere on the window, you *randomize* the contents of the
picture. By *randomize* we mean, you set the value of each pixel in the 'picture' to True or False, randomly.
For an example, see a screenshot of how this could look in the "noise.png" picture.

For clarity, add the code that randomizes the content in a function called ``add_noise``.
This should be reflected in the drawn picture too (you should call ``draw_picture`` and ``draw_grid`` after each
event). If you need a refresh on how to handle mouse events, refer to
[MoreMouseInputWithLists.py](../../week02-event-driven-programming/step0204/MoreMouseInputWithLists.py) step 0204 from
week 2.
