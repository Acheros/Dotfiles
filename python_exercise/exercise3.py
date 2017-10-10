#!/usr/bin/python3

"""input a number to calculate"""
n = input("please input a number to compute: ")
n = int(n)
d = dict()
for i in range(1, n+1):
    d[i] = i*i

print(d)
