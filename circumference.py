def calculate_circumference(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * 3.14 * radius

radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print("The circumference of the circle is: ",circumference)