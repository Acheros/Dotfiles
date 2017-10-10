#!/usr/bin/python3

# input
input_a = input('please enter input_a:')
input_b = input('please enter input_b:')
input_c = input('please enter input_c:')
input_a = int(input_a)
input_b = int(input_b)
input_c = int(input_c)
# compare 2 input


def compare_max(a, b):
    if a < b:
        print('the largest number is b: ', end='')
        print(input_b)
    else:
        if a == b:
            print('two number are equal to each other: ', end='')
            print(input_a)
        else:
            print('the largest number is a: ', end='')
            print(input_a)

# compare 3 input


def compare_max_3(a, b, c):
    if a < c and b < c:
        print('the largest number is c:', end='')
        print(input_c)
    else:
        if a < b:
            print('the largest number is b:', end='')
            print(input_b)
        else:
            print('the largest number is a:', end='')
            print(input_a)
# compare function


compare_max_3(input_a, input_b, input_c)
