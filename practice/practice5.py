#!/usr/bin/python3

# input the first and last name
input_firstname = input('please enter your first name: ')
input_lastname = input('please enter your lastname: ')
input_firstname = str(input_firstname)
input_lastname = str(input_lastname)

# print out the result
print('the reverse of your first name and last name is: ', end='')
print(input_lastname + ' ' + input_firstname)
