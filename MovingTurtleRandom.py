# Moving Turtle

# Required Modules
import turtle as t
import random as rd  # for ramdom motion

# Shape as turtle
t.shape('turtle')

# Set fill color
t.fillcolor("blue")

# Bg color
t.bgcolor("black")

# turtle speed
t.speed('slow')

def inside_window():
    left_limit = (-t.window_width()/2) + 100  # left boundary
    right_limit = (t.window_width()/2) - 100
    top_limit = (t.window_height()/2) - 100
    bottom_limit = (-t.window_height()/2) + 100
    (x,y) = t.pos()
    inside = (left_limit < x < right_limit) and (bottom_limit < y < top_limit)
    return inside

def MoveTurtle():
    if inside_window():
        angle = rd.randint(0,180)
        t.right(angle)
        fd = rd.randint(10,100)
        t.forward(fd)
    else:
        t.backward(200)

while True:
    MoveTurtle()
    
