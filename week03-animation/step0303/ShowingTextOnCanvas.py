# This program adds to the previous animation by adding text too.

from tkinter import *

WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 10
DELAY = 20  # delay between animations, in milliseconds

win = Tk()  # as before, creates a window
win.title('Simple animation over both axis, with text')

# ball data
ball_x = WIDTH/2
ball_y = HEIGHT/2
ball_r = BALL_RADIUS
# the ball_speed_x determines the rate by which the X coordinate of the ball changes
ball_speed_x = 5
ball_speed_y = 5

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

ball = canvas.create_oval(ball_x - ball_r, ball_y - ball_r, ball_x + ball_r, ball_y + ball_r, fill='red', outline='black')
# The 'canvas' can also draw text. Here we add text at the top-center of the window, and save its ID.
text_id = canvas.create_text(WIDTH/2, 30, text='Direction', font=('Arial Bold', 12), fill='green')


def animation():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    # The following lines of code ensure that the ball bounces back when it hits the right/left and top/bottom
    # boundaries of the window.
    # Note that by taking BALL_RADIUS into our calculations, we make the ball bounce as soon as it touches the edges.
    if ball_x >= WIDTH - BALL_RADIUS:
        ball_speed_x = -abs(ball_speed_x)
    if ball_x <= BALL_RADIUS:
        ball_speed_x = abs(ball_speed_x)
    if ball_y >= HEIGHT - BALL_RADIUS:
        ball_speed_y = -abs(ball_speed_y)
    if ball_y <= BALL_RADIUS:
        ball_speed_y = abs(ball_speed_y)
    canvas.coords(ball, ball_x-ball_r, ball_y-ball_r, ball_x+ball_r, ball_y+ball_r)
    # In the next 2 lines we use the ternary conditional operator, similar to the '?' in Java.
    # You can learn more about this at: https://docs.python.org/3/reference/expressions.html#conditional-expressions
    # Below, we use the ternary conditional operator to determine the direction of the ball (up/down, and left/right),
    # to then use it to update the text in the canvas.
    up_down = 'up' if ball_speed_y < 0 else 'down'
    canvas.itemconfig(text_id, text='Direction: ' + up_down, font=('Arial Bold', 12), fill='green')
    # Todo 1. Update the code so that the text shows the direction on both axis, e.g. up/left, down/right, etc.
    canvas.after(DELAY, animation)


animation()

win.mainloop()  # listens for events, such as key presses and mouse clicks
