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
    def to_json_string(list_dictionaries):
        """ Returns JSON string rep of list_dictionaries
        """
        import json
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string rep of list_objs to file
        """
        import json
        dictlist = []
        filename = cls.__name__
        a = vars(list_objs[0])
        b = vars(list_objs[1])
        dictlist.append(a)
        dictlist.append(b)
        with open("{}.json".format(filename), mode='w', encoding='utf-8') as f:
            f.write(Base.to_json_string(dictlist))

    @classmethod
    def _reset_nb_objects(cls):
        """ For testing only, hook in setUp to reset class-level id num
        """
        cls.__nb_objects = 0
