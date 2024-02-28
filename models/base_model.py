#!/usr/bin/python3
"""Defines the BaseModel Class."""
import models
from datetime import datetime
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()

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
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """BaseModel Constructor.

        Args:
            *args (any): wont be used.
            **kwargs (dict): Pairs attributes
        """
        id = str(uuid4())
        created_at = datetime.utcnow()
        updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """Update updat_at with currrent datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return the dict Representasion of the Class."""
        dict_r = self.__dict__.copy()
        dict_r["__class__"] = str(type(self).__name__)
        dict_r["created_at"] = self.created_at.isoformat()
        dict_r["updated_at"] = self.updated_at.isoformat()
        dict_r.pop("_sa_instance_state", None)
        return dict_r
    
    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)
        
    def __str__(self):
        """Return the str representation of the BaseModel."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
    
