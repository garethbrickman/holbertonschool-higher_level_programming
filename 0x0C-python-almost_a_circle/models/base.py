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
        """ Returns list of JSON string representation
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
        if not list_dictionaries:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attrs set
        """
        dummy = cls(width=1, height=1, x=0, y=0)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances
        """
        pass

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string rep of list_objs to file
        """
        fm = cls.__name__
        empty = []
        dictlist = []
        dictlist2 = []
        if not list_objs:
            with open("{}.json".format(fm), mode='w', encoding='utf-8') as f:
                f.write(Base.to_json_string(empty))
        else:
            for x in list_objs:
                dictlist.append(vars(x))
            with open("{}.json".format(fm), mode='w', encoding='utf-8') as f:
                newf = (Base.to_json_string(dictlist))
                newf = (newf.replace('_Rectangle__', ''))
                f.write(newf)

    @classmethod
    def load_from_file(cls):
        """ Returns list of instances
        """
        pass

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes to csv
        """
        pass

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes from csv
        """
        pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws all recs and squares
        """
        pass

    @classmethod
    def _reset_nb_objects(cls):
        """ For testing only, hook in setUp to reset class-level id num
        """
        cls.__nb_objects = 0
