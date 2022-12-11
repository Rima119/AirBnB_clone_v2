#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import json
import pep8
from models.user import User
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        fs = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(fs.total_errors, 0, "fix pep8")

    def test_new(self):
        """ New object is correctly added to __objects """
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = "wed3eefef"
        user.name = "hello"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_all(self):
        """ __objects is properly returned """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
