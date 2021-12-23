# WAP to draw four different squares.

import turtle

def FILL(x):
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)
FILL(20)
FILL(40)
FILL(60)
FILL(100)
