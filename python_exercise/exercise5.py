#!/usr/bin/python3
n = input('please input a maximize to do the math:')
n = int(n)
d = dict()

for i in range(1, n+1):
    d[i] = i * i

print(d)
