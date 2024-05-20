#!/usr/bin/python3
''' create unique FileStorage'''
import models
from models.base_model import BaseModel
import models.engine
import models.engine.file_storage
storage = models.engine.file_storage.FileStorage()
storage.reload()
