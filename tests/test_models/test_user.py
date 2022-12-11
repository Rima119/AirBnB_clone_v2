#!/usr/bin/python3
""" unittests for models/user.py """
from models.base_model import BaseModel
from models.user import User
import unittest
from datetime import datetime
import os
import pep8


class TestUser(unittest.TestCase):
    """ Unittests for testing the user model """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()

    def test_pep8_User(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        u = style.check_files(['models/user.py'])
        self.assertEqual(u.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_is_subclass_User(self):
        """check if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_User(self):
        """check attribute type for User Class"""
        us = User(email="hello@hello.com", password="hello")
        self.assertEqual(str, type(us.id))
        self.assertEqual(datetime, type(us.created_at))
        self.assertEqual(datetime, type(us.updated_at))
        self.assertTrue(hasattr(us, "__tablename__"))
        self.assertTrue(hasattr(us, "email"))
        self.assertTrue(hasattr(us, "password"))
        self.assertTrue(hasattr(us, "first_name"))
        self.assertTrue(hasattr(us, "last_name"))
        self.assertTrue(hasattr(us, "places"))
        self.assertTrue(hasattr(us, "reviews"))

    def test_to_dict_User(self):
        """check if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
