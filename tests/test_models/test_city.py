#!/usr/bin/python3
"""unnittests for models/city.py"""
from models.base_model import Base, BaseModel
from models.city import City
from datetime import datetime
import unittest
import os
import pep8


class TestCity(unittest.TestCase):
    """Unittests for testing the City model"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        c = style.check_files(['models/city.py'])
        self.assertEqual(c.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Check for attributes type"""
        ct = City()
        self.assertEqual(str, type(ct.id))
        self.assertEqual(datetime, type(ct.created_at))
        self.assertEqual(datetime, type(ct.updated_at))
        self.assertTrue(hasattr(ct, "__tablename__"))
        self.assertTrue(hasattr(ct, "name"))
        self.assertTrue(hasattr(ct, "state_id"))


if __name__ == "__main__":
    unittest.main()
