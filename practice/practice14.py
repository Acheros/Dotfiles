#!/usr/bin/python3

import math


"""calculate the volume of the sphere"""

radius = int(input("please input a radius: "))
Volume = 4 / 3 * math.pi * pow(radius, 3)
print("the volume of the sphere is:", Volume)
