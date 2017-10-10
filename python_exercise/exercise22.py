#!/usr/bin/python3

import re
password = [str(x) for x in input("please input a sequence of input seperate by a coma: ").split(",")]


def getmix(passwords):
    mix_list = []
    for i in passwords:
        upper = int(len(set(re.findall(r'[A-Z]', i))))
        lower = int(len(set(re.findall(r'[a-z]', i))))
        numbs = int(len(set(re.findall(r'[0-9]', i))))
        symbo = int(len(set(re.findall(r'[$#@]', i))))
        if 6 < len(i) < 12 and upper >= 1 and lower >= 1 and numbs >= 1 and symbo >= 1:
            mix_list.append(i)
        else:
            pass
    return mix_list


print(",".join(getmix(password)))
