#!/usr/bin/python3
"""First Class"""
"""let's test user class"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    
    def test_user(self):
        """let's check attributes of class user"""
        usr = User()
        self.assertTrue(hasattr(usr, "id"))
        self.assertIsInstance(usr.id, str)
        self.assertTrue(hasattr(usr, "created_at"))
        self.assertIsInstance(usr.created_at, datetime)
        self.assertTrue(hasattr(usr, "updated_at"))
        self.assertIsInstance(usr.updated_at, datetime)
        self.assertTrue(hasattr(usr, "email"))
        self.assertIsInstance(usr.email, str)
        self.assertTrue(hasattr(usr, "password"))
        self.assertIsInstance(usr.password, str)
        self.assertTrue(hasattr(usr, "first_name"))
        self.assertIsInstance(usr.first_name, str)
        self.assertTrue(hasattr(usr, "last_name"))
        self.assertIsInstance(usr.last_name, str)


if __name__ == "__main__":
    unittest.main()
