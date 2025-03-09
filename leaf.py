import turtle
import math

def leaf(turtle, size):
    """
    Draws a leaf shape using two semi-circles.
    """
    for i in range(2):
        turtle.circle(size, 90)
        turtle.circle(size // 2, 90)

def position_turtle(turtle, length):
    """
    Moves the turtle to the starting position for drawing the leaf.
    """
    turtle.penup()
    turtle.right(180)
    turtle.forward(length / 2)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()

def draw_leaf(size):
    """
    Sets up the turtle and draws the leaf.
    """
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.color("green")
    position_turtle(pen, size)
    leaf(pen, size)
    turtle.done()

# Example usage:
draw_leaf(100)