#!/usr/bin/python3

file_name = open("/proc/cpuinfo", "r")


def check_cpu(file_new):
    i = 0
    for line in file_new:
        if set("processor").issubset(line):
            i += 1
        else:
            i = i
    return i


print("the number of processor is using:", check_cpu(file_name))
file_name.close()
