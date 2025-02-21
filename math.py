import math

#Task 1
def convert_degree_to_radian():
    degree = float(input("Input degree: "))
    radian = degree * (math.pi / 180)
    print(f"Output radian: {radian:.6f}")

#Task 2
def calculate_trapezoid_area():
    height = float(input("Height: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))
    area = 0.5 * (base1 + base2) * height
    print(f"Expected Output: {area}")

#Task 3
def calculate_polygon_area():
    num_sides = int(input("Input number of sides: "))
    side_length = float(input("Input the length of a side: "))
    area = int((num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides)))
    print(f"The area of the polygon is: {area}")

#Task 4
def calculate_parallelogram_area():
    base_length = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
    area = base_length * height
    print(f"Expected Output: {area}")

convert_degree_to_radian()
calculate_trapezoid_area()
calculate_polygon_area()
calculate_parallelogram_area()
