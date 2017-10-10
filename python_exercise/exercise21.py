#!/usr/bin/python3

print("Enter your content and press Ctrl-d to save it: ")
contents = []
while True:
    try:
        line = input("")
    except EOFError:
        break
    contents.append(line)

your_value = 0
for value in contents:
    new_value = value.split(" ")
    if new_value[0] == "D":
        your_value += int(new_value[1])
    elif new_value[0] == "W":
        your_value -= int(new_value[1])

print("your net amount =", your_value)
