#!/usr/bin/python3
""" unittests for models/place.py """
from models.base_model import Base, BaseModel
from models.place import Place
import unittest
from datetime import datetime
import os
import pep8


class TestPlace(unittest.TestCase):
    """Unittests for testing the Place model"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.place = Place()

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Place(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """Check for attributes types"""
        pl = Place()
        self.assertEqual(str, type(pl.id))
        self.assertEqual(datetime, type(pl.created_at))
        self.assertEqual(datetime, type(pl.updated_at))
        self.assertTrue(hasattr(pl, "__tablename__"))
        self.assertTrue(hasattr(pl, "city_id"))
        self.assertTrue(hasattr(pl, "name"))
        self.assertTrue(hasattr(pl, "description"))
        self.assertTrue(hasattr(pl, "number_rooms"))
        self.assertTrue(hasattr(pl, "number_bathrooms"))
        self.assertTrue(hasattr(pl, "max_guest"))
        self.assertTrue(hasattr(pl, "price_by_night"))
        self.assertTrue(hasattr(pl, "latitude"))
        self.assertTrue(hasattr(pl, "longitude"))


if __name__ == "__main__":
    unittest.main()
