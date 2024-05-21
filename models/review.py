#!/usr/bin/python3
"""Module with review class"""
import models

class Review(models.BaseModel):
	"""خاص بالمراجعه"""
	place_id = ""
	user_id = ""
	text = ""
