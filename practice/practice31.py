#!/usr/bin/python3

a = int(input("please input a number: "))
b = int(input("please input a number: "))
c = int(input("please input a number: "))

tong = a + b + c
if a == b or b == c or c == a:
    tong = 0
elif 15 <= tong <= 20:
    tong = 20
print("the sum of 3 numbers: ", tong)
