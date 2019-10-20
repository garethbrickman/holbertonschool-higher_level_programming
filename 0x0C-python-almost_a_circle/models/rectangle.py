#!/usr/bin/python3
""" Rectangle class module
"""
from models.base import Base
import operator

class Rectangle(Base):
    """ Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Returns area of instance
        """
        return self.__width * self.__height

    def display(self):
        """ Prints with # to stdout
        """
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            for y in range(self.__y):
                print()
            for i in range(self.__height):
                for x in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print()

        # print("\n".join(["#"*self.__width] * self.__height))

    def __str__(self):
        """ Updates class Rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    """ Getters and Setters
    """

    width = property(operator.attrgetter('width'))

    @width.setter
    def width(self, v):
        """ Setter
        """
        if type(v) is not int: raise TypeError("width must be an integer")
        if v <= 0: raise ValueError("width must be > 0")
        self.__width = v

    height = property(operator.attrgetter('height'))

    @height.setter
    def height(self, v):
        """ Setter
        """
        if type(v) is not int: raise TypeError("height must be an integer")
        if v <= 0: raise ValueError("height must be > 0")
        self.__height = v

    x = property(operator.attrgetter('x'))

    @x.setter
    def x(self, v):
        """ Setter
        """
        if type(v) is not int: raise TypeError("x must be an integer")
        if v < 0: raise ValueError("x must be >= 0")
        self.__x = v

    y = property(operator.attrgetter('y'))

    @y.setter
    def y(self, v):
        """ Setter
        """
        if type(v) is not int: raise TypeError("y must be an integer")
        if v < 0: raise ValueError("y must be >= 0")
        self.__y = v
