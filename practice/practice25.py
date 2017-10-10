#!/usr/bin/python3


this_list = input("please input a list of string seperate by a coma: ").split(",")          # noqa
new_list = [str(n) for n in this_list]

string = ""
for i in new_list:
    string = string + i

print(string)
