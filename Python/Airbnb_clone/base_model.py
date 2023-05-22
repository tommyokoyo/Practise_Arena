#!/usr/bin/python3
""" This describes the common attr/methods for other classes"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Base Model of project"""

    def __init__(self, *args, **kwargs):
        """ Initalizes a new Instance of the base model
            Args:
                args (any): takes any type and save in tuple
                kwargs (dict): key value pair of args passed
        """
        if kwargs:
            for m, n in kwargs.items():
                if m == "created_at" or m == "updated_at":
                    self.__dict__[m] = datetime.strptime(n, "%Y-%m-%dT%H:%M:%S.%f")
                
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    
    def __str__(self) -> str:
        """ Returns a string rep of the Basemodel instance"""
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
    def to_dict(self) -> dict:
        """ Returns a dict containing values of the __dict__instance"""
        my_Instance = self.__dict__.copy()
        my_Instance["__class__"] = self.__class__.__name__
        my_Instance["created_at"] = self.created_at.isoformat()
        my_Instance["updated_at"] = self.updated_at.isoformat()

        return my_Instance
