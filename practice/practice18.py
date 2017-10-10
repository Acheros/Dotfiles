#!/usr/bin/python3

string_input = str(input("please input a string: "))

check = string_input.split(" ")
if check[0] == 'is':
    print(string_input)
else:
    print('is', string_input)
