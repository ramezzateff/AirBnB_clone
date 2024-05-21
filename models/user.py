#!/usr/bin/python3
"""module creates User class"""
from models.base_model import BaseModel
class User(BaseModel):
	"""
    Inherting from BaseModel
    Setting class attribute
    """
	email = ""
	password = ""
	first_name = ""
	last_name = ""
