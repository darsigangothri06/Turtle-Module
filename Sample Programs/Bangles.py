import turtle

turtle.bgcolor('black')
colors = ["blue","red", "yellow", "violet", "green"]
turtle.speed(100)

for i in range(1,90):
    turtle.color(colors[i%len(colors)])
    turtle.circle(i+90)
    turtle.left(10)
