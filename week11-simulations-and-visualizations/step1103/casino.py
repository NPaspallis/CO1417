# Casino simulation
import random
from tkinter import *

# the French roulette has 37 slots: 18 red, 18 black, and 1 green - you can concatenate lists with the + operator
ROULETTE_COLORS = ['red' for i in range(16)] + ['black' for j in range(16)] + ['green']


def spin_the_roulette() -> str:
    """
    Returns one of 'red', 'black', 'green' in random, using the ROULETTE_COLORS chances.
    """
    return random.choice(ROULETTE_COLORS)


TITLE = 'Roulette simulation'
WIDTH = 800
HEIGHT = 600
BASELINE = HEIGHT - 10

# Create the Window.
win = Tk()
win.title(TITLE)
win.geometry(str(WIDTH) + "x" + str(HEIGHT))

# Create and pack the canvas.
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

# Simulation parameters
DELAY = 10
TARGET = 512
current_round = 0  # counts how many rounds (bets) have gone so far - initially zero
text_object = canvas.create_text(WIDTH-30, HEIGHT-20, text='0')  # This is the text object to hold the balance
balance = 256  # current balance - initially set to 256 units which allows for at least 8 spins before you run out of money
bet = 1  # current bet, initially set to 1 unit


def play():
    """
    Implements the following betting algorithm:
    - Bet 1 unit
    - If you lose, double the bet and try again
    - If you win, add the cash to the balance, and reset the bet to 1
    Continue until you either reach your target, or go broke.
    At the same time, for every round draw a line showing the progress of the balance.
    """
    global balance, current_round, bet
    current_round = current_round + 1
    canvas.itemconfig(text_object, text=str(current_round))

    old_balance = balance  # remember current balance, so you can draw the line to the new balance
    color = spin_the_roulette()  # we always bet on 'red'
    if color == 'red':  # won!
        balance = balance + bet  # cash the win
        print('won €', bet, ', balance: €', balance)
        bet = 1  # reset bet to €1
    else:  # when color is not 'red' ('black' or 'green'), we lose
        balance = balance - bet  # decrease the balance by bet
        print('lost :-( €', bet, ', balance: €', balance)

    canvas.create_line(current_round, BASELINE - old_balance, current_round + 1, BASELINE - balance)  # draw the balance line
    if balance < bet:  # not enough money to place the bet - Lost :-(
        print("LOST :-(")
        return
    if balance >= TARGET:  # you have reached your target! - Won :-)
        print("WON :-)")
        return
    win.after(DELAY, play)


# draw base-line
canvas.create_line(0, BASELINE, WIDTH, BASELINE, fill='red')
# draw win-line
canvas.create_line(0, HEIGHT-TARGET-10, WIDTH, HEIGHT-TARGET-10, fill='green')
win.after(0, play)

win.bind('Q', quit)
win.bind('q', quit)

win.mainloop()  # listens for events, such as key presses and mouse clicks
