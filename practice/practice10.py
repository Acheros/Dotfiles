#!/usr/bin/python3

date = input('please input a date for schedule with a coma: ')

new_date = date.split(",")

print("the exam date: " + new_date[0] + "/" + new_date[1] + "/" + new_date[2])
