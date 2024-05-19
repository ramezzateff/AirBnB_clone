#!/usr/bin/python3
'''That module created Review class '''
from models.base_model import base_model


class Review(BaseModel):
	"""Class for managing reeivew objects"""

	place_id = ''
	user_id = ''
	text = ''