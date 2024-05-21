#!/usr/bin/python3
"""BaseModel defines attributes and methods for all"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Base class for inheritance by all other classes"""
    
    def __init__(self, *args, **kwargs):
        """Sets up instance attributes during initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """update instance attribute updateds"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns copy of dictionary
        added '__class__' key
        Update time  with isoformat
        """
        cop = self.__dict__.copy()
        cop["__class__"] = type(self).__name__
        cop["created_at"] = self.created_at.isoformat()
        cop["updated_at"] = self.updated_at.isoformat()
        return cop

    def __str__(self):
        """Prints Classname, instance id, and dictionary"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
