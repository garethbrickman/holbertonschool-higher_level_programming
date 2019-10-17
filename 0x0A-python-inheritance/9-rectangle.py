#!/usr/bin/python3
"""
     Class for BaseGeometry
"""


class BaseGeometry:
    """Defines base class"""

    def area(self):
        """Return area"""
        pass

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
"""
     Class for Rectangle
"""


class Rectangle(BaseGeometry):
    """Defines rectangle class"""

    def __init__(self, width, height):
        """Instantiation"""
        super().__init__()
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def __str__(self):
        """Prints rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
