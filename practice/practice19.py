#!/usr/bin/python3


def calculate(str, n):
    final_str = ''
    for i in range(n):
        final_str = final_str + " " + str
    return final_str


string = str(input("please input a string: "))
number = int(input("please input an integer number: "))
print(calculate(string, number))
