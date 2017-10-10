#!/usr/bin/python3

print("Enter your content and press Ctrl-d to save it: ")
contents = []
while True:
    try:
        line = input("")
    except EOFError:
        break
    contents.append(line)

list_str = [element.upper() for element in contents]
for i in list_str:
    print(i)
