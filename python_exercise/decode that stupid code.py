#!/usr/bin/python3
file = open(r"/home/haxerl/Downloads/faces.txt", "r", encoding="utf-8-sig")

from collections import Counter
wordcount = Counter(file.read().split())

for item in wordcount.items():
    print("{}\t{}".format(*item))
