#!/usr/bin/python3
""" Module holds Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        with open(cls.__name__ + 'json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                MyList = []
                for i in list_objs:
                    MyList.append(i.to_dictionary())
                f.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with attributes already set """
        if cls.__name__ == "Rectangle":
            dummy_c = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_c = cls(1)
        dummy_c.update(**dictionary)
        return (dummy_c)
