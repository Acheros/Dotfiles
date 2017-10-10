#!/usr/bin/python3


def near_thousand(number):
    if abs(1000 - number) <= 100 or abs(2000 - number) <= 100:
        return True
    else:
        return False


"""main function"""
number1 = int(input("please input a number: "))
if near_thousand(number1):
    print("it is a number near 1000 or 2000")
else:
    print("it is not a number near 1000 or 2000")
