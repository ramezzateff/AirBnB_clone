#!/usr/bin/python3
"""init all the package as lib"""
import models
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
