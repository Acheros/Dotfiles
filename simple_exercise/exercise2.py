#!/usr/bin/python3

# input
hello = ['hello', 'world', ['damn', 'new right']]
# print len of the string

"""print length of a single chracter"""
def lenght(string_a):
    i = 0
    a = 0
    for i in string_a:
        a = a + 1
    print(a)
# print len in general case


def lenght_general(string_b):
    for each_string in string_b:
        """check if there is a list in each string"""
        if isinstance(each_string, list):
            lenght_general(each_string)
        else:
            print('the number in string: ', end='')
            print(each_string, end='')
            print(' is ', end='')
            lenght(each_string)

# print length text


lenght_general(hello)
