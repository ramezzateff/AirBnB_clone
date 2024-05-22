#!/usr/bin/python3
"""Module with review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """خاص بالمراجعه"""
    place_id = ""
    user_id = ""
    text = ""
