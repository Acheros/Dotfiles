#!/usr/bin/python3


def count_num_4(numbers):
    count = 0
    for number in new_list:
        number = int(number)
        if number == 4:
            count = count + 1
    return count


list_number = input("please in put a list a of number seperate by a coma: ")
new_list = list_number.split(",")
print(count_num_4(new_list))
