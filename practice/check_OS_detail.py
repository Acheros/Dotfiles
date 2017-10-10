#!/usr/bin/python3


file_name = open("/proc/version", "r")


def check_system():
    for line in file_name:
        if set('64').issubset(line):
            print("this is a 64-bit system")
        else:
            print("this is a 32-bit system")


def print_OS():
    for lines in file_name:
        print(lines)


print("choose option 1 to see if this it a 32-bit or 64-bit system")
print("choose option 2 to see your OS detail")
a = str(input("please choose an option: "))
if a == "1":
    check_system()
elif a == "2":
    print_OS()
else:
    print("please input a valid option")
