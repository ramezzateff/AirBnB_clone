#!/usr/bin/python3
'''This model creates a User class'''
from models.base_model import base_model


class user(BaseModel):
	'''Clas for managing user objects'''

	email = ''
	password = ''
	first_name = ''
	last_name = ''