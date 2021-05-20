# This program calculates area of a circle as per radius provided by the input.

import math

print("Calculate area of a circle")
print("==========================")
radius = input("Enter the value of radius: ")
area = math.pi * pow(float(radius), 2)
print("The calculated area of circle is ", area)
