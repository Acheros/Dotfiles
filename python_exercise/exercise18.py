#!/usr/bin/python3

input_str = input("please input a string: ")

UPPERCASE = 0
LOWERCASE = 0

for i in input_str:
    if i.isupper():
        UPPERCASE += 1
    elif i.islower():
        LOWERCASE += 1
    else:
        pass

print("UPPERCASE", UPPERCASE)
print("LOWERCASE", LOWERCASE)
