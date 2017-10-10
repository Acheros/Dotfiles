#!/usr/bin/python3

values = input("please input a list of number: ")
numbers = [x for x in values.split(",") if int(x) % 2 != 0]
print(",".join(numbers))
