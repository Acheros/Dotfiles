#!/usr/bin/python3

number = input("please input a integer number: ")

try:
    numbers = int(number)
except:
    print("please input an integer")
else:
    number = int(number)
    if 0 < number < 10:
        hundred = number * 100 + number * 10 + number
        two_number = number * 10 + number
        hundred = int(hundred)
        two_number = int(two_number)
        print(hundred + two_number + number)
    else:
        print("the input must be between 1 and 9")
