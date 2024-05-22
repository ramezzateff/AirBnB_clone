#!/usr/bin/python3
"""it module creates a amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Inherting from BaseModelSetting class attribute"""
    name = ""
