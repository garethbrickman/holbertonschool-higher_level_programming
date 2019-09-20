#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared2 = []
    for x in range(len(matrix)):
        squared = []
        for y in range(len(matrix[x])):
            squared.append(matrix[x][y] ** 2)
        squared2.append(squared)
    return squared2
# [[x**2 for x in row] for row in matrix]
