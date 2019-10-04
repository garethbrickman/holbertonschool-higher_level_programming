#!/usr/bin/python3
"""
     Module for print_square functions


"""


def print_square(size):
    """ Say name function

    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size >= 0:
        size = int(size)
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        pass
    else:
        for x in range(size):
            for y in range(size):
                print("#", end="")
            print()
