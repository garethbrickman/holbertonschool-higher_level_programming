#!/usr/bin/python3
""" Square class model
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def to_dictionary(self):
        """ Makes dict representation
        """
        dictrep = {}
        dictrep['id'] = self.id
        dictrep['size'] = self.size
        dictrep['x'] = self.x
        dictrep['y'] = self.y
        return dictrep

    def __str__(self):
        """ Updates class Square
        """
        return("[{}] ({}) {}/{} - {}".format((self.__class__.__name__),
                                             self.id, self.x,
                                             self.y, self.size))

    def update(self, *args, **kwargs):
        """ Assigns new arguments to each attribute
        """

        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    """ Getters and Setters
    """

    @property
    def size(self):
        """ Getter
        """
        return self.__width

    @size.setter
    def size(self, v):
        """ Setter
        """
        if type(v) is not int:
            raise TypeError("width must be an integer")
        if v <= 0:
            raise ValueError("width must be > 0")
        self.__width = v
        self.__height = v
