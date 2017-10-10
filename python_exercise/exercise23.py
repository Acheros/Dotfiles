#!/usr/bin/python3

from operator import itemgetter

list_name = []
while True:
    try:
        a = input("please input a name, age, high: ").split(",")
    except EOFError:
        break
    list_name.append(tuple(a))

sort_name = sorted(list_name, key=itemgetter(0, 1, 2))
print("")
print("new list: ", sort_name)
