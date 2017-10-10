#!/usr/bin/python3

number = int(input("please input a number: "))
new_list = input("please input a list of number: ")
new_list = new_list.split(",")


def get_number_list():                      # get number list_number
    list_number = []
    for i in new_list:
        numbers = int(i)
        list_number.append(numbers)
    return list_number


def check_number(numbers, number_list):              # check if the number is in the list # noqa
    for i in number_list:
        if numbers == i:
            return True
        else:
            return False


print(check_number(number, get_number_list()))
