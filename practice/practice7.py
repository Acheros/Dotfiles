#!/usr/bin/python3

import os
import pty

values = input('input some value seperate by a comma: ')
list = values.split(",")
tuple = tuple(list)
print('list: ', list)
print('tuple: ', tuple)
