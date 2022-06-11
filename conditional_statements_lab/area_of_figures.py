from math import pi
figures_type = input()
result = 0
if figures_type == "square":
    side = float(input())
    result = side * side
elif figures_type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    result = side_a * side_b
elif figures_type == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
elif figures_type == "triangle":
    side = float(input())
    height = float(input())
    result = side * height/ 2
print(f"{result:.3f}")