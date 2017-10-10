#!/usr/bin/python3

input_str = input("please input a sentence: ").split()
wordcounter = {}

# loop to make a list and tuple
for word in input_str:
    if word not in wordcounter:
        wordcounter[word] = 1
    else:
        wordcounter[word] += 1

# print out word
for item in wordcounter.items():
    print("{}\t{}".format(*item))
