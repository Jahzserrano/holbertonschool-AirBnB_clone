#!/usr/bin/python3
"""Defines the BaseModel Class."""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel Class

    Attributes:
        id (String): BaseModel id
        created_at (DateTime): assign with the current datetime when an instance is created.
        updated_at (DateTime): assign with the current datetime when an instance is created and it will be updated every time you change your object
    """
    
    id = str(uuid4())
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()
    
    
    def save(self):
        """Update updat_at"""
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        """Return the dict Representasion of the Class"""
        dict_r = self.__dict__.copy()
        dict_r["__class__"] = str(type(self).__name__)
        dict_r["created_at"] = self.created_at.isoformat()
        dict_r["updated_at"] = self.updated_at.isoformat()
        dict_r.pop("_sa_instance_state", None)
        return dict_r
    
    def __str__(self):
        """Return the str representation of the BaseModel"""
        dic = self.__dict__.copy()
        dic.pop("_sa_instance_state", None)
        return f"[{type(self).__name__}] ({self.id}) {dic}"
    