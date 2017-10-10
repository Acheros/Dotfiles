#!/usr/bin/python3

str_input = str(input("please input letters and digits: "))

letters = 0
digits = 0

for i in str_input:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
    else:
        pass

print("LETTERS", letters)
print("DIGITS", digits)
