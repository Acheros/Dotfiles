#!/usr/bin/python3

chracter = str(input('please input a chracter: '))
if len(chracter) == 1:
    chracter = chracter.lower()
    if [chracter == 'a'
     or chracter == 'e'
     or chracter == 'i'
     or chracter == 'o'
     or chracter == 'u']:                                           # noqa
        print("the input chracter is a vowel")
    else:
        print("it is not a vowel")
