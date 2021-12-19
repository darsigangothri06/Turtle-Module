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