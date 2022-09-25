#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 09.25.22
# This program calculates the area and perimeter of
# a rectangle with user input.

import math
from tkinter import N
from turtle import width

Length = input("What is the length of your rectangle?: ")
width = input("What is the width of your rectangle?: ")
rect_length = int(Length)
rect_width = int(width)
print ("P = (L+w)*2")
print ("A = L*W")
Perimeter = (rect_length + rect_width)*2
Area = rect_length * rect_width

print("The perimeter is {} cm". format(Perimeter))
print("The area is {} cm^2". format(Area))
