#!/usr/bin/python3
"""module creates User class"""
import models
class User(models.BaseModel):
	"""
    Inherting from BaseModel
    Setting class attribute
    """
	email = ""
	password = ""
	first_name = ""
	last_name = ""
