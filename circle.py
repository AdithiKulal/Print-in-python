class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14 * (self.radius ** 2), 2)

    def perimeter(self):
        return round(2 * 3.14 * self.radius, 2)

radius=float(input("Enter the radiius: "))
circle=Circle(radius)
print("Radius:", circle.radius)
print("Area:", circle.area())
print("Circumference:", circle.perimeter())