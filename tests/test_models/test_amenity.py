#!/usr/bin/python3
"""unittests for models/amenity.py"""
from models.base_model import Base, BaseModel
from models.amenity import Amenity
import unittest
from datetime import datetime
import os
import pep8


class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity model"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        a = style.check_files(['models/amenity.py'])
        self.assertEqual(a.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """Check for attributes type"""
        am = Amenity()
        self.assertEqual(str, type(am.id))
        self.assertEqual(datetime, type(am.created_at))
        self.assertEqual(datetime, type(am.updated_at))
        self.assertTrue(hasattr(am, "__tablename__"))
        self.assertTrue(hasattr(am, "name"))
        self.assertTrue(hasattr(am, "place_amenities"))


if __name__ == "__main__":
    unittest.main()
