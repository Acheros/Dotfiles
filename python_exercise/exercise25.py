#!/usr/bin/python3


def putNumbers(n):
    for i in range(0, int(n)):
        if int(i) % 7 == 0:
            return i


a = putNumbers(100)


for i in a:
    print(i)
