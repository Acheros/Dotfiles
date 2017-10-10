#!/usr/bin/python3

import math

point_A = input("please input vector number: ")
point_B = input("please input vector number: ")

list_A = point_A.split(",")
list_B = point_B.split(",")
xA = float(list_A[0])
yA = float(list_A[1])
xB = float(list_B[0])
yB = float(list_B[1])

distance = math.hypot(xA - xB, yA - yB)

print(distance)
