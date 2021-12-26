import turtle

colors = ['blue', 'pink', 'yellow', 'orange', 'green', 'red', 'grey']
c = len(colors)
for i in range(10,50,5):
    turtle.circle(i)
    turtle.color(colors[i%c])
