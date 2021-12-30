# This program demonstrates how to realize animations over both X-Y axes in a 2-D graphical application

from tkinter import *

WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 10
DELAY = 20  # delay between animations, in milliseconds

win = Tk()  # as before, creates a window
win.title('Simple animation over both axis')

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


def animation():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    # The following lines of code ensure that the ball bounces back when it hits the right/left and top/bottom
    # boundaries of the window.
    # Note that by taking BALL_RADIUS into our calculations, we make the ball bounce as soon as it touches the edges.
    if ball_x >= WIDTH-BALL_RADIUS:
        ball_speed_x = -abs(ball_speed_x)  # the 'abs' computes the absolute value - why is it needed?
    if ball_x <= BALL_RADIUS:
        ball_speed_x = abs(ball_speed_x)
    if ball_y >= HEIGHT - BALL_RADIUS:
        ball_speed_y = -abs(ball_speed_y)
    if ball_y <= BALL_RADIUS:
        ball_speed_y = 0
    canvas.coords(ball, ball_x-ball_r, ball_y-ball_r, ball_x+ball_r, ball_y+ball_r)
    # Todo 1. This function has a bug: When the ball reaches the top of the window, it's stuck there. Can you fix this
    #   so that the ball bounces on the top as well?
    canvas.after(DELAY, animation)


animation()

win.mainloop()  # listens for events, such as key presses and mouse clicks
