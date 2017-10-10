#!/usr/bin/python3

valueses = input('input a full name of a file: ')
list = valueses.split(".", 1)
if len(list) < 2:
    print('please input a proper file name')
else:
    print(list[len(list)-1])
