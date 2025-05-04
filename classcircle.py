class Shape:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        return f"This is a {self.name}."

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")  # Call the parent constructor
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius  # Correcting the syntax error

circle = Circle(5)
print(circle.info())
print(f"Area of the circle: {circle.area()}")