#!/usr/bin/python3
"""Defines the BaseModel Class."""
import models
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """BaseModel Class

    Attributes:
        id (String): BaseModel id
        created_at (DateTime): assign with the current datetime
        when an instance is created.
        updated_at (DateTime): assign with the current datetime when an
        instance is created and it will be updated every time you change
        your object
    """
    
    def __init__(self, *args, **kwargs):
        """BaseModel Constructor.

        Args:
            *args (any): wont be used.
            **kwargs (dict): Pairs attributes
        """
        id = str(uuid4())
        created_at = datetime.today()
        updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update updat_at with currrent datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dict Representasion of the Class."""
        dict_r = self.__dict__.copy()
        dict_r["__class__"] = self.__class__.__name__
        dict_r["created_at"] = self.created_at.isoformat()
        dict_r["updated_at"] = self.updated_at.isoformat()
        return dict_r
    
    def __str__(self):
        """Return the str representation of the BaseModel."""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
    
