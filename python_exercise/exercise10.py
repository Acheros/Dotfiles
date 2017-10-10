#!/usr/bin/python3

row_column = input("please input row and column: ")
dimension = [int(i) for i in row_column.split(',')]
dimension_row = dimension[0]
dimension_column = dimension[1]
Matrix = [[0 for x in range(dimension_column)] for y in range(dimension_row)]

for row in range(dimension_row):
    for column in range(dimension_column):
        Matrix[row][column] = row * column

print(Matrix)
