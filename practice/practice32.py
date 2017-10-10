#!/usr/bin/python3

PV = int(input("please input present value: "))
number = float(input("please input rate of interest: "))
years = int(input("please input a years: "))

total = PV*((1 + number / 100) ** years)
print(total)
