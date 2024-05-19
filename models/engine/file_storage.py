#!/usr/bin/python3
'''Module for FileStorageclass.'''
import json
import os

class FileStorage:
    '''Class that stores and retrieves data'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id'''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path)'''
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        '''Reloads the stored objects'''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
            obj_dict = json.load(f)
            from models.base_model import BaseModel
            FileStorage.__objects = {k: BaseModel(**v) for k, v in obj_dict.items()}

