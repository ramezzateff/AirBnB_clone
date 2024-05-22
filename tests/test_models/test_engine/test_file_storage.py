#!/usr/bin/python3
"""let's test FileStorage class"""
import unittest
from models.base_model import BaseModel
import models
import os
import json


class TestFileStorage(unittest.TestCase):
	"""let's gooooooooooooooooo"""
    def test_FileStorage_init(self):
        filepath = models.storage._FileStorage__file_path
        _objs = models.storage._FileStorage__objects
        """first check its attributes"""
        self.assertEqual(filepath, "file.json")
        self.assertIsInstance(filepath, str)
        self.assertIsInstance(_objs, dict)
        new = BaseModel()
        """ check methods """
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        """test all function"""
        self.assertIsInstance(models.storage.all(), dict)
        self.assertNotEqual(models.storage.all(), {})
        """check if id is found"""
        self.assertTrue(hasattr(new, "id"))
        self.assertIsInstance(new.id, str)

        """test new function"""
        key = "BaseModel."+new.id
        self.assertIsInstance(models.storage.all()[key], BaseModel)
        self.assertEqual(models.storage.all()[key], new)
        """ check if object exist by key """
        self.assertIn(key, models.storage.all())
        """ check if the object found in storage with correct id"""
        self.assertTrue(models.storage.all()[key] is new)

        """test save function"""
        models.storage.save()
        with open(filepath, 'r') as file:
            saved_data = json.load(file)
        """ check if object exist by keyname """
        self.assertIn(key, saved_data)
        """ check if the value found in json is correct"""
        self.assertEqual(saved_data[key], new.to_dict())

        """test reload function"""
        models.storage.all().clear()
        models.storage.reload()
        with open(filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data[key],
                         models.storage.all()[key].to_dict())

        """file"""
        if os.path.exists(filepath):
            os.remove(filepath)
        self.assertFalse(os.path.exists(filepath))
        models.storage.reload()


if __name__ == '__main__':
    unittest.main()
