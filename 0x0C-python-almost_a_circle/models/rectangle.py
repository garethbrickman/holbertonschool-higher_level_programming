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

    width = property(operator.attrgetter('__width'))

    @width.setter
    def width(self, v):
        """ Setter
        """
        if type(v) is not int: raise TypeError("width must be an integer")
        if v <= 0: raise ValueError("width must be > 0")
        self.__width = v

    height = property(operator.attrgetter('__height'))

    @height.setter
    def height(self, v):
        """ Setter
        """
        if type(v) is not int: raise TypeError("height must be an integer")
        if v <= 0: raise ValueError("height must be > 0")
        self.__height = v

    x = property(operator.attrgetter('__x'))

    @x.setter
    def x(self, v):
        """ Setter
        """
        if type(v) is not int: raise TypeError("x must be an integer")
        if v < 0: raise ValueError("x must be >= 0")
        self.__x = v

    y = property(operator.attrgetter('__x'))

    @y.setter
    def y(self, v):
        """ Setter
        """
        if type(v) is not int: raise TypeError("y must be an integer")
        if v < 0: raise ValueError("y must be >= 0")
        self.__y = v
