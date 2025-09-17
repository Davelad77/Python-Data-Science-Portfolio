# ask the user to enter the lengths of all 3 sides of a triangle
# calculate and display the area of the triangle

import math
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
semi_perimeter = (side1 + side2 + side3) / 2
area_triangle = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
print("The area of the triangle is: ", area_triangle)