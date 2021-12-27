# Creating a robot
import turtle as t

# creating a rectangle
def Rect(breadth, length, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(breadth)
        t.right(90)
        t.forward(length)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor("Dodger blue")

# Left Foot
t.goto(-100,-150)
Rect(50,20,"blue")

# Right Foot
t.goto(-30,-150)
Rect(50,20,"blue")

# Right Leg
t.goto(-25,-50)
Rect(15,100,"grey")

# Left Leg
t.goto(-70,-50)
Rect(15,100,"grey")

# Body
t.goto(-90,100)
Rect(100,150,'red')

# Left Arm
t.goto(-150,70)
Rect(60,15,'grey')

# Left Hand
t.goto(-150,110)
Rect(15,40,'grey')

# Right Arm
t.goto(10,70)
Rect(60,15,'grey')

# Right Hand
t.goto(55,110)
Rect(15,40,'grey')

# Neck
t.goto(-50,120)
Rect(15,20,'grey')

# Face
t.goto(-85,170)
Rect(80,50,'red')

# Eyes
t.goto(-60,160)
Rect(30,10,'white')

# Eyeballs
t.goto(-55,155)
Rect(5,5,'black')

t.goto(-40,155)
Rect(5,5,'black')

# Mouth
t.goto(-65,130)
Rect(40,5,'black')

t.goto(-40,-250)
t.color('white')
t.write("HELLO,I AM HARSHINI", align = 'center', font = ('Arial',30,'bold'))

t.hideturtle()  # hiding the cursor
