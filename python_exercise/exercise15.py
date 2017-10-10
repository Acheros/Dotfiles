#!/usr/bin/python3

binary = input("please input a 4 number binary seperate by a coma: ")

list_binary = binary.split(",")

check_5 = []
for i in list_binary:
    decimal = 0
    for n in i:
        if n == "1":
            decimal = decimal * 2 + 1
        elif n == "0":
            decimal = decimal * 2
    if decimal % 5 == 0:
        check_5.append(i)

print(','.join(check_5))
