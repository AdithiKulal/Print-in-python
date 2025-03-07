import turtle
turtle.Screen().bgcolor("salmon")
turtle.Screen().setup(300, 300)
triangle=turtle.Turtle()
num_sides=3
side_length=50
angle = 360.0 / num_sides
for i in range(num_sides):
    triangle.color("navy")
    triangle.forward(side_length)  
    triangle.left(angle)
turtle.done()