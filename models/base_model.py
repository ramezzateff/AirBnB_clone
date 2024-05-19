#!/usr/bin/python3
''' This script is the base model'''

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    '''The Parent of all classes'''

    def __init__(self, *args, **kwargs):
        '''Initialize instance attributes'''
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        '''Return the class name & id & dict of attributes'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''Updates the public instance attribute updated_at with the current datetime'''
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of __dict__'''
        data_rep = self.__dict__.copy()
        data_rep['__class__'] = self.__class__.__name__
        data_rep['created_at'] = self.created_at.isoformat()
        data_rep['updated_at'] = self.updated_at.isoformat()
        return data_rep

