#!/usr/bin/python3
'''Module for FileStorage'''
import json
import os
from .. import base_model


class FileStorage:
    '''class that store and get out the data'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''

        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with
        key <obj class name>.id '''

        key = ("{}.{}".format(type(obj).__name__, obj.id))
        FileStorage.__object[key] = obj

    def save(self):
        '''serializes __objects to
        the JSON file (path: __file_path)'''

        with (FileStorage.__file_path, 'w', encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in self.__object.items()}
            jason.dump(d, f)

    def reload(self):
        '''deserializes the JSON file to __objects'''
