#!/usr/bin/python3

number1 = int(input('please input the first number: '))
number2 = int(input('please input the second number: '))
number3 = int(input('please input the third number: '))

if number1 == number2 == number3:
    total = (number1 + number2 + number3) * 3
else:
    total = number1 + number2 + number3

print('the toal of three number is:', total)
