#!/usr/bin/python3
"""Initializes the package"""
from models.engine.file_storage import FileStorage
import models
storage = FileStorage()
storage.reload()
