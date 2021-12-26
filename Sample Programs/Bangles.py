import turtle

colors = ["blue","red"]
turtle.speed(100)
for i in range(1,120):
    turtle.color(colors[i%len(colors)])
    turtle.circle(i+90)
    turtle.left(10)
