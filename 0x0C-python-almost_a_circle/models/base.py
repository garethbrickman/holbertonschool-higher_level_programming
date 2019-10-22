#!/usr/bin/python3
""" Base class model
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

    @staticmethod
    def from_json_string(json_string):
        """ Returns list of JSON string rep
        """
        from json import loads as l
        newlist = []
        if json_string is None or len(json_string) < 1:
            return newlist
        else:
            newlist = l(json_string)
            return newlist

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON string rep of list_dictionaries
        """
        import json
        string = "[]"
        if len(list_dictionaries) < 1 or list_dictionaries is None:
            return string
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attrs set
        """
        pass

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string rep of list_objs to file
        """
        import json
        filename = cls.__name__
        dictlist = []
        for x in list_objs:
            dictlist.append(vars(x))
        with open("{}.json".format(filename), mode='w', encoding='utf-8') as f:
            f.write(Base.to_json_string(dictlist))

    @classmethod
    def _reset_nb_objects(cls):
        """ For testing only, hook in setUp to reset class-level id num
        """
        cls.__nb_objects = 0
