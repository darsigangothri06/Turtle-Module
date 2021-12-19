# Drawing a circle using turtle.circle()
import turtle

turtle.circle(50)  # drawing a circle of radius 50 pixels

# Moving turtle to (90,90)
turtle.penup()
turtle.goto(90,90)

turtle.pendown()
turtle.circle(90,180)  # extent = 180 degrees, turtle draws a semi circle

turtle.penup()
turtle.goto(-120,90)

turtle.pendown()
turtle.circle(70,steps = 6)  # drawing a hexagon

