#!/usr/bin/python3
""" Rectangle class model
"""
from models.base import Base


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

    def to_dictionary(self):
        """ Makes dict representation
        """
        dictrep = {}
        dictrep['id'] = self.id
        dictrep['width'] = self.width
        dictrep['height'] = self.height
        dictrep['x'] = self.x
        dictrep['y'] = self.y
        return dictrep

    def update(self, *args, **kwargs):
        """ Assigns new arguments to each attribute
        """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

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
        return("[{}] ({}) {}/{} - {}/{}".format((self.__class__.__name__), self
                                                .id, self.__x, self.__y, self._
                                                _width, self.__height))

    """ Getters and Setters
    """

    @property
    def width(self):
        """ Getter
        """
        return self.__width

    @width.setter
    def width(self, v):
        """ Setter
        """
        if type(v) is not int:
            raise TypeError("width must be an integer")
        if v <= 0:
            raise ValueError("width must be > 0")
        self.__width = v

    @property
    def height(self):
        """ Getter
        """
        return self.__height

    @height.setter
    def height(self, v):
        """ Setter
        """
        if type(v) is not int:
            raise TypeError("height must be an integer")
        if v <= 0:
            raise ValueError("height must be > 0")
        self.__height = v

    @property
    def x(self):
        """ Getter
        """
        return self.__x

    @x.setter
    def x(self, v):
        """ Setter
        """
        if type(v) is not int:
            raise TypeError("x must be an integer")
        if v < 0:
            raise ValueError("x must be >= 0")
        self.__x = v

    @property
    def y(self):
        """ Getter
        """
        return self.__y

    @y.setter
    def y(self, v):
        """ Setter
        """
        if type(v) is not int:
            raise TypeError("y must be an integer")
        if v < 0:
            raise ValueError("y must be >= 0")
        self.__y = v
