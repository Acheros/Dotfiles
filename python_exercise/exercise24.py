#!/usr/bin/python3

import math

contents = []
print("please input a set of instruction:")


while True:
    try:
        a = input("")
    except EOFError:
        break
    contents.append(a)


x = 0
y = 0
distant = 0


for value in contents:
    new_value = value.split(" ")
    if new_value[0] == "UP":
        y += int(new_value[1])
    elif new_value[0] == "DOWN":
        y -= int(new_value[1])
    elif new_value[0] == "RIGHT":
        x += int(new_value[1])
    elif new_value[0] == "LEFT":
        x -= int(new_value[1])


distant = math.hypot(x, y)
print("the distant is:", distant)
