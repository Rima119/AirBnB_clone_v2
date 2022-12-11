#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
from datetime import datetime
import pep8
from uuid import UUID
import json
import os
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """base_model unittests"""

    @classmethod
    def setUpClass(cls):
        """ """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        style = pep8.StyleGuide(quiet=True)
        b = style.check_files(['models/base_model.py'])
        self.assertEqual(b.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """check for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """test attributes"""
        self.assertEqual(str, type(self.base.id))
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_init(self):
        """Test initialization"""
        self.assertIsInstance(self.base, BaseModel)

    def test_method_BaseModel(self):
        """test methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_to_dict_BaseModel(self):
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
