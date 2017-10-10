#!/usr/bin/python3

# input a number n
n = input('please enter a number to factorize: ')
n = int(n)
if n == 0:
    print('0')
A = 1
for i in range(1, (n+1)):
    A = A * i

print(A)
