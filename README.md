## Turtle Graphics

* importing turtle module `import turtle`
  
Show the current location of the turtle using `turtle.showturtle()`

Turtle is like a `pen`. The arrowhead indicates the current position and direction of the pen.

Initially, the turtle is positioned at the center of the window.

## Moving the Turtle in any direction

`turtle` is an object which is created when we import the turtle module.

As soon as the object is created its position is set at (0,0), i.e. at the center of the turtle window.

Also by default, its direction is set to go straight to the right.

### Pen

The imported turtle module uses a pen to draw shapes. It can be used to move and draw lines in any direction.

Python contains methods for moving the pem, setting the pen's size, lifting and putting the pen down.

* By default, the pen is down.

| Method Name | Meaning | Syntax |
| :---: | :---: | --- |
| `Forward` | Moves the turtle P pixels in the direction of its current heading.| `turtle.forward(P)` |
| `Left` | Rotates the turtle left by specified angle. | `turtle.left(angle)` |
| `Right` | Rotates the turtle in place a degree clockwise. | `turtle.right(angle)` |
| `Backward` | Moves the turtle P pixels in the direction opposite to its current heading.| `turtle.backword(P)` |
| `Pen down` | Pulls the pen down. Draws when it moves from one place to the other. | `turtle.pendown()` |
| `Pen up` | Pulls the pen up. It just moves from one place to the other without drawing anything. | `turtle.penup()` |
| `Pen size` | Sets the line thickness to the specified width. | `turtle.pensize()` |

## Moving turtle to any location

The turtle's arrowhead is at the center of the graphics window at coordinate(0,0).

The method `goto(x,y)` is used to move the turtle at specified points (x,y).


## The COLOR, BGCOLOR, CIRCLE AND SPEED METHOD OF TURTLE

| Method Name | Meaning | Syntax
| :---: | :---: | :---: |
| `Speed` | The drawing speed of the turtle must be in the range int 1 (slowest) to 10 (fastest) or 0 (instantaneous) | `turtle.speed()`
| `Circle` | Draws a circle with the given radius. The center is radius units left of the turtle. The extent determines which part of the circle is drawn. If it is not given, the entire circle is drawn. | `turtle.circle(radius,extent = None)` |
| `Color` | The color method is used to draw colorful animations. | `turtle.color(*args)` |
| `BG color` | Returns the background color of the turtle screen. | `turtle.bgcolor(*arg)` |

## Drawing with Colors

| Method Name | Meaning | Syntax |
| :---: | :---: | :---: |
| `Color` | Sets the pen's color | `turtle.color(c)` |
| `FillColor` | Sets the pen's fill color to 'C' | `turtle.fillcolor(C)` |
| `Begin Fill` | Calls this method before filling a shape. | `turtle.begin_fill()` |
| `End Fill` | Fills the shape drawn before the last call to begin_fill | `turtle.end_fill()` |
| `Filling` | Returns the fill state. True is filling, False if not filling. | `turtle.filling()` |
| `Clear` | Clears the window. The state and position of window is not affected. | `turtle.clear()` |
| `Reset` | Clears the window and reset the state and position to its original default value. | `turtle.reset()` |
| `Screensize` | Sets the width and height of the canvas | `turtle.screensize()` |
| `Show Turtle` | Makes the turtle visible. | `turtle.showturtle()` |
| `Hide Turtle` | Makes the turtle invisible. | `turtle.hideturtle` |
| `Turtle Write` | Writes a message on the turtle graphics window. | `turtle.write(msg)` |
