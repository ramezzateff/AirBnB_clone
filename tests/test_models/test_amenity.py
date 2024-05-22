#!/usr/bin/python3
"""let's test amenity class"""
"""fifth class"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):

    def test_amenity(self):
        """let's start checking its attributes"""
        am = Amenity()
        self.assertTrue(hasattr(am, 'id'))
        self.assertIsInstance(am.id, str)
        self.assertTrue(hasattr(am, 'created_at'))
        self.assertIsInstance(am.created_at, datetime)
        self.assertTrue(hasattr(am, 'updated_at'))
        self.assertIsInstance(am.updated_at, datetime)
        self.assertTrue(hasattr(am, 'name'))
        self.assertIsInstance(am.name, str)


if __name__ == '__main__':
    unittest.main()
