#!/usr/bin/python3
'''Module for FileStorage'''
import json


class FileStorage:
    '''class that store and get out the data'''

    __file_path = file.json
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with
        key <obj class name>.id '''
        key = (f"<{type(obj).__name__}>.{obj.id}")
        FileStorage.__object[key] = obj

    def save(self):
        '''serializes __objects to
        the JSON file (path: __file_path)'''

    def reload(self):
        '''deserializes the JSON file to __objects'''
