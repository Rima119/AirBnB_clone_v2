#!/usr/bin/python3
""" Unittests for models/review.py """
from models.base_model import Base, BaseModel
from models.review import Review
import unittest
import os
import pep8


class TestReview(unittest.TestCase):
    """ Unittests for testing the Review model """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.rev = Review()

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        r = style.check_files(['models/review.py'])
        self.assertEqual(r.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_is_subclass_Review(self):
        """check if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
