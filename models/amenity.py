#!/usr/bin/python3
"""Defining class Amenity"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name: str = ""
