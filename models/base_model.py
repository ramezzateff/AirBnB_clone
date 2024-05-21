#!/usr/bin/python3
"""BaseModel defines attributes and methods for all"""
import uuid
from datetime import datetime
class BaseModel:
    """Base class for inheritance by all other classes"""
    def __init__(self, *args, **kwargs):
        """Sets up instance attributes during initialization

        args:
            - *args: list of arguments
            - **kwargs __dict__ of key:values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "createds":
                    self.__dict__["createds"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updateds":
                    self.__dict__["updateds"] = datetime.strptime(
                        kwargs["updateds"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())

        self.created_at = datetime.now()
        print(f"time of createds \n{self.created_at}")
        self.update_at = datetime.now()
        print(f"time updates \n{self.update_at}")

    def save(self):
        """update instance attribute updateds"""
        self.update_at = datetime.now()
        storage.save()

    
    def to_dict(self):
        """
        returns copy of dictionary
        added '__class__' key
        Update time  with isoformat
        """
        cop = self.__dict__.copy()
        cop["__class__"] = type(self).__name__
        cop["created"] = datetime.isoformat(self.created_at)
        cop["update"] = self.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return cop

    def __str__(self):
        """Prints Classname, instance id, and dictionary"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
