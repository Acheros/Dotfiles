#!/usr/bin/python3

import math

numbers = input("please input a list of number: ")
new_numbers = numbers.split(",")


def get_number_list():                      # get number list_number
    list_number = []
    for i in new_numbers:
        number = int(i)
        list_number.append(number)
    return list_number


for i in get_number_list():
    Q = math.floor(math.sqrt((2 * 50 * i) / 30))
    print(Q)
