#!/usr/bin/python3
''' create unique FileStorage'''
import models
import models.engine
import models.engine.file_storage
storage = models.engine.file_storage.FileStorage()
storage.reload()
