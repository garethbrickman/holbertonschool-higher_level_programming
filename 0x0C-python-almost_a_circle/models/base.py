#!/usr/bin/python3
""" Base class module
"""


class Base:
    """ Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def _reset_nb_objects(cls):
        """ For testing only, hook in setUp to reset class-level id num
        """
        cls.__nb_objects = 0
