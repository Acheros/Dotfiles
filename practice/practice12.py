#!/usr/bin/python3
"""import calender"""

import calendar


""" begin main """
while True:
    month = int(input("please input a month: "))
    year = int(input("please input a year: "))
    try:
        print(calendar.monthcalendar(year, month))
        break
    except ValueError:
        print('please input a proper month')
