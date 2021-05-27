# This program calculates area of a circle as per radius provided by the input.

import math


def calculate_area():
    radius = input("Enter the value of radius: ")
    area_c = math.pi * pow(float(radius), 2)
    return area_c


def print_area():
    print("Calculate area of a circle")
    print("==========================")
    area = calculate_area()
    print("The calculated area of circle is ", area)


print_area()
