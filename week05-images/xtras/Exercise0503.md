# Exercise 0503 - Scaling pictures

This is a challenge: Try to define a function:
``def draw_scaled_bitmap(bitmap_array_2d, foreground_color, background_color, target_width, target_height)``
where the bitmap is drawn to the targeted width and height.

This is simpler when the target width and height are multiples of the original dimensions of the bitmap (e.g.,
when they are double) but much more complex when not. Another challenge is when the target dimension is smaller
than the original. In this case you could use your own algorithm to decide the color of a scaled down pixel.
Once implemented, try this function for at least the double and half dimensions of the original.
