#!/usr/bin/python3

input_list = input("please input a list seperate by a comma: ")
input_list = [str(i) for i in input_list.split(",")]

new_list = sorted(input_list)

for i in new_list:
    print(i, ",", end="")
