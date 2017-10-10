#!/usr/bin/python3


def sum_recursive(n):
    S = 0
    for i in range(0, n + 1):
        S = S + i
    return S


numbers = int(input("please input a number: "))
print(sum_recursive(numbers))
