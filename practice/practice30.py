#!/usr/bin/python3

# greatest common divisor


def gcm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# least common multiple of 2 numbers


def lcm(a, b):
    c = a * b
    d = c / gcm(a, b)
    return d

# main function


print("choose number 1 if you want to use greatest common divisor")
print("choose number 2 if you want to use least common multiple")
a = str(input("input your choose: "))
if a == '1':
    num1 = int(input("input a number: "))
    num2 = int(input("input a number: "))
    print("the greatest common divisor:", gcm(num1, num2))
elif a == '2':
    num3 = int(input("input a number: "))
    num4 = int(input("input a number: "))
    print("the least common multiple:", lcm(num3, num4))
else:
    print("please input a valid option")
