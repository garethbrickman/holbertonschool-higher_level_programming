#!/usr/bin/python3
"""
     Module for matrix_divided functions


"""


def matrix_divided(matrix, div):
    """ Divide matrix function

    """
    count = len(matrix)
    errmess = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(errmess)
    while count > -1:
        if len(matrix[0]) != len(matrix[count-1]):
            raise TypeError("Each row of the matrix must have the same size")
        count -= 1

    newmatrix2 = []
    for x in range(len(matrix)):
        newmatrix = []
        for y in range(len(matrix[x])):
            newmatrix.append(round(matrix[x][y] / div, 2))
        newmatrix2.append(newmatrix)
    return newmatrix2
