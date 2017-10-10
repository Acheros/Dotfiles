#!/usr/bin/python3


old_list = []


def isAllEven(n):
    sum_number = 0
    n = str(n)
    for i in n:
        i = int(i)
        if i % 2 == 0:
            sum_number += 1
    if sum_number == len(n):
        return(n)


for i in range(1000, 3001):
    if isAllEven(i) is None:
        pass
    else:
        print(isAllEven(i))
