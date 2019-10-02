#!/usr/bin/python3
class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Optional instantiation for size, must be int and >= 0"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns current square area"""
        return (self.__size * self.__size)
