#!/usr/bin/python3

name = input('please input the full name of your file: ')
namesplit = name.split(".")
if (sum(x is not None for x in namesplit)) == 2:
    print(namesplit[-1])
else:
    print('PLEASE INPUT a FULL PROPER FILE NAME')
