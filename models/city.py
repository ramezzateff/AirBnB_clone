#!/usr/bin/python3
"""its module"""
import models
from models.base_model import BaseModel

class City(models.BaseModel):
	"""its City"""
	state_id = ""
	name = ""
