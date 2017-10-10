#!/usr/bin/python3

r_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def  make_more_word():
    new_list=[]
    for i in r_list_1:
        if any(i in word for word in color_list_2):
            new_list.append(i)
    return new_list

print(make_more_word())

