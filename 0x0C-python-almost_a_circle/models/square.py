#!/usr/bin/python3
""" Square class module
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Updates class Square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)
