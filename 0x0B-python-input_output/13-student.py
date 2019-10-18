#!/usr/bin/python3
""" Student class module
"""


class Student:
    """ Student class
    """
    def __init__(self, first_name, last_name, age):
        """ Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Makes dict representation
        """
        x = vars(self)
        return x

    def reload_from_json(self, json):
