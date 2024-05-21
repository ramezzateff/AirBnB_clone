#!/usr/bin/python3
"""it module creates a amenity class"""
from models.base_model import BaseModel
import models
class Amenity(models.BaseModel):
	"""Inherting from BaseModelSetting class attribute"""
	name = ""
