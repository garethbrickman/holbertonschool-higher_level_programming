#!/usr/bin/python3
"""
     Class for defining a rectangle


"""

class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation with optional width & height (must be int and >= 0)
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns area"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter"""
        if self.width == 0:
            perim = 0
        elif self.height == 0:
            perim = 0
        else:
            perim = (self.width * 2) + (self.height * 2)
        return perim

    def __str__(self):
        """Returns print rectangle as object readable"""
        return "\n".join(["#"*self.width] * self.height)

    def __repr__(self):
        """Returns print rectangle as reproduced object"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Prints msg when instance of Rectangle is deleted"""
        print ("Bye rectangle...")
        type(self).number_of_instances -= 1
