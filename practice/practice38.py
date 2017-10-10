#!/usr/bin/python3
import os.path
import time

file = input("please input path file: ")
print("last modified: %s" % time.ctime(os.path.getmtime(file)))
print("created: %s" % time.ctime(os.path.getctime(file)))
