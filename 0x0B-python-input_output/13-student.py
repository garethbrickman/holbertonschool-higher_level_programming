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
        dict2 = {}
        x = vars(self)
        if attrs is None:
            return x
        for key, val in x.items():
            if key in attrs:
                dict2[key] = val
        return dict2

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance
        """
        attrs = "first_name, last_name, age"
        for key, val in json.items():
            if key in attrs:
                    setattr(self, key, val)
