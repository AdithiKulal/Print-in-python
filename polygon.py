import turtle
turtle.Screen().bgcolor("salmon")
turtle.Screen().setup(300,300)
polygon = turtle. Turtle() 
num_sides = int(input("Enter the number of sides: "))
side_length = 50
angle = 360.0 / num_sides
for i in range(num_sides):
  polygon.color("navy")
  polygon.backward(side_length)
  polygon.left(angle)
turtle.done()