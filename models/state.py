#!/usr/bin/python3
"""Defining class State"""
from models.base_model import BaseModel

class State(BaseModel):
    """State class that inherits from BaseModel."""
    name: str = ""
