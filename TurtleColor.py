import turtle
'''
turtle.color()
    ---> Returns or set the pencolor and fillcolor
    ---> color()
        ---> Return the current pencolor and the current fillcolor as a pair of color specification strings.
    ---> color(colorstring), color((r,g,b)), color(r,g,b)
        ---> inputs as in pencolor, set both, fillcolor and pencolor to the given value.
    ---> color(colorstring1, colorstring2), color((r,g,b),(r,g,b))
        ---> Equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
'''
print(turtle.color()) # black

turtle.color("blue") # pencolor = fillcolor = blue
turtle.circle(40)

turtle.penup()
turtle.goto(90,90)
turtle.pendown()

turtle.color("red","blue") # pencolor = red and fillcolor = blue
turtle.circle(50)
