#!/usr/bin/python3
''' create unique FileStorage'''
import models
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
