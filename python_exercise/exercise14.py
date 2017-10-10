#!/usr/bin/python3

string_input = input("Please input a string: ")
list_input = [str(i) for i in string_input.split(",")]

list_input = list(set(list_input))

new_input = sorted(list_input)

print(" ".join(new_input))
