#!/usr/bin/python3

import datetime
import time
from datetime import date


def subtract_2_date(date1, date2):
    time_between = abs(date1 - date2)
    returnvalue = time_between.days
    return returnvalue


"""begin main"""
while True:
    # input variable
    day1 = int(input("please input the first day: "))
    month1 = int(input("please input the first month: "))
    year1 = int(input("please input the first year: "))
    day2 = int(input("please input the second day: "))
    month2 = int(input("please input the second month: "))
    year2 = int(input("please input the second month: "))
    # begin testing if the input is right
    try:
        date1 = date(year1, month1, day1)
        date2 = date(year2, month2, day2)
        print("the date between them is: " +
              str(subtract_2_date(date1, date2)))
        break
    except ValueError:
        print("please input a proper date")
