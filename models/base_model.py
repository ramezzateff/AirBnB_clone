#!/usr/bin/python3
''' This script is the base model'''
import uuid
import datetime


class BaseModel:
    '''The Parent of all classes'''
    def __init__(self, *args, **kwargs):
        '''Initialize instance attributes

        Args:
        *args: list of arguments
        **kwargs: a dict of key-value arguments
        '''
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'id':
                    self.id = value
                elif key not in '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()

    def __str__(self):
        '''Return the class name & id & dict of attribute'''

        return "[{}] ({}) {}"./
    format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''Updates the public instance attribute updated
        _at with the current datetime'''

        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of __dict__'''

        data_Rep = self.__dict__.copy()
        data_Rep['__class__'] = self.__class__.__name__
        data_Rep['created_at'] = data_Rep['created_at'].isoformat()
        data_Rep['updated_at'] = data_Rep['updated_at'].isoformat()

        return data_Rep
