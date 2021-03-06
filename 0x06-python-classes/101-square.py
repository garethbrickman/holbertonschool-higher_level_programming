#!/usr/bin/python3
class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size (must be int and >= 0)
        and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Getter"""
        return self.__position

    @position.setter
    def position(self, position):
        """Setter"""
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(tuple) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[0], int) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[1], int) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Returns current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                    print("#", end="")
            print()

    def __str__(self):
        """Returns print square as object readable"""
        return (
            "\n"*self.position[1] +
            " " * self.position[0] +
            "#" * self.size
            )
