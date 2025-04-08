import math

def calculate_trigonometric_values(angle):
    angle_in_radians = math.radians(angle)
    sin_value = math.sin(angle_in_radians)
    cos_value = math.cos(angle_in_radians)
    tan_value = math.tan(angle_in_radians)
    return sin_value, cos_value, tan_value

angle = float(input("Enter an angle in degrees: "))

sin_value, cos_value, tan_value = calculate_trigonometric_values(angle)

print(f"Sin({angle}°) = {sin_value:.4f}")
print(f"Cos({angle}°) = {cos_value:.4f}")
print(f"Tan({angle}°) = {tan_value:.4f}")