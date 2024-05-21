#!/usr/bin/python3
"""module creates User class"""
import models
from models.base_model import BaseModel
class User(models.BaseModel):
	"""
    Inherting from BaseModel
    Setting class attribute
    """
	email = ""
	password = ""
	first_name = ""
	last_name = ""
