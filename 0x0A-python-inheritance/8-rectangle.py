#!/usr/bin/python3
"""
     Class for BaseGeometry
"""


class BaseGeometry:
    """Defines base class"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines rectangle class"""

    def __init__(self, width, height):
        """Instantiation"""
        self.__width = Rectangle.integer_validator(self, "width", width)
        self.__height = Rectangle.integer_validator(self, "height", height)
