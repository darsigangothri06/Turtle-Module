import turtle as t

t.penup()
t.goto(-100,100)
x = -100
y = 100

t.penup()

for i in range(1,11):
    y = y - 20
    for j in range(1,11):
        t.speed(1)
        t.write(i*j)
        t.forward(20)
    t.goto(x,y)
