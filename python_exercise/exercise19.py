#!/usr/bin/python3

a = input("please input a number: ")

n1 = int("%s%s%s%s" % (a, a, a, a))
n2 = int("%s%s%s" % (a, a, a))
n3 = int("%s%s" % (a, a))
n4 = int("%s" % a)

numbers = n1 + n2 + n3 + n4
print(numbers)
