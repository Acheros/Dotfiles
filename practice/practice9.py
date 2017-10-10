#!/usr/bin/python3

str_color_list = input('please input some color seperate by a space: ')
color_list = str_color_list.split(" ")
print(color_list[1])
print(color_list[len(color_list) - 1])
