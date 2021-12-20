import turtle

turtle.forward(50)
turtle.color("blue")

turtle.begin_fill()
print(turtle.filling()) # True
turtle.circle(50)
turtle.end_fill()

print(turtle.filling()) # False
