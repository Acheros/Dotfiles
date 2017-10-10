#!/usr/bin/python3


class inputandoutput(object):
    def __init__(self):
        self.a = ""

    def getinput(self):
        self.a = input("please input a word: ")

    def returnoutput(self):
        print(self.a)


Object = inputandoutput()
Object.getinput()
Object.returnoutput()
