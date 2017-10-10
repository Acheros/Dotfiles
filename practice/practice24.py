#!/usr/bin/python3

from collections import Counter


def input_number():
    num = input("please input a list of number: ").split(",")
    return [int(n) for n in num]


x = input_number()
d = Counter(x)

print(d)
