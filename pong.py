# Pong Game
# Author: Bhargava Gumpula
# Start Date: 07/19/2020
# End Date: ??/??/2020

from tkinter import *
from paddle import *
from ball import *
import time
import random
import sys

def end_game(event):
   sys.exit()

tk = Tk()
def game_start():
  red_ball = Ball(20, 'red', canvas, tk, paddle)
  while True:
    red_ball.draw()
    tk.update_idletasks()
    tk.update()

# Main program
tk.title("Pong Game")

# Draw the canvas
canvas = Canvas(tk, height=1000, width=1000)
canvas.pack()

# Draw the Paddle
paddle = Paddle(canvas)
paddle.draw()
canvas.bind_all('<Key-Right>', paddle.movepaddle)
canvas.bind_all('<Key-Left>', paddle.movepaddle)
canvas.bind_all('<Key-Down>', paddle.movepaddle)

game_start()
raw_input("PRESS ANY KEY TO EXIT:")

