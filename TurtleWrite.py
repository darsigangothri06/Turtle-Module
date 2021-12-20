import turtle

'''
Syntax: write(arg, move = False, align = 'left', font = ('Arial', 8, 'normal')
    ---> arg -- info, which is to be written to the turtlescreen
    ---> move(optional) -- True/False
    ---> align (optional) -- one of the strings "left", "center" or "right"
    ---> font (optional) -- a triple (fontname, fontsize, fonttype)
'''
turtle.write("HELLO")

turtle.penup()
turtle.forward(50)
turtle.pendown()

turtle.write(arg = "Hello", move = True)  # move = True draws a line.

turtle.penup()
turtle.forward(50)
turtle.pendown()

turtle.write(arg = "Hello", move = False, align = "center") 

turtle.penup()
turtle.forward(80)
turtle.pendown()

turtle.write(arg = "Hello", move = False, align = "center", font = ("Arial", 40, "bold")) 
