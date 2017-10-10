#!/usr/bin/python3

number1 = int(input("please input a number: "))
subtract = 17 - number1

if subtract < 0:
    abs_subtract = abs(subtract) * 2
    print("the answer is:", abs_subtract)
else:
    print("the answer is:", subtract)
