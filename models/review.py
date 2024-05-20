#!/usr/bin/python3
'''That module created Review class '''
import models


class Review(models.BaseModel):
    """Class for managing reeivew objects"""

    place_id = ''
    user_id = ''
    text = ''
