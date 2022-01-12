# Exercise 0101

Create a program to draw all squares with sides 100, 110, 120, ..., 300, centered at the center of a window with size 800x600.
You must use the *while loop* option to realize the main loop.

See this image for what the output is expected to be like:
![co-centric squares](https://raw.githubusercontent.com/NPaspallis/CO1417/main/week01-drawing-colored-shapes/xtras/Exercise0101.png)

Hints:
- See: https://www.w3schools.com/python/python_while_loops.asp
- You can use `canvas.create_rectangle(left, top, right, bottom)`
where left, top, right, bottom are the coordinates of the left-top and right-bottom corners of
the rectangle to be drawn

Optional:
- Define a function which takes as arguments the coordinates of the center of the square, and draws it.
Then edit your code to use this function.
