#!/usr/bin/python3

lines = []
s = []
while True:
    if len(s) <= 2:
        s = input("please input a text: ")
    else:
        s = input("please input another text if need: ")
    if s:
        lines.append(s.upper())
    else:
        break
for letter in lines:
    print(letter)
