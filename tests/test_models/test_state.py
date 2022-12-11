#!/usr/bin/python3
""" unittests for models/state.py """
from models.base_model import Base, BaseModel
from models.state import State
from datetime import datetime
import unittest
import os
import pep8


class TestState(unittest.TestCase):
    """ Unittests for testing the State model """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.state = State()

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """Check for attributes type"""
        st = State()
        self.assertEqual(str, type(st.id))
        self.assertEqual(datetime, type(st.created_at))
        self.assertEqual(datetime, type(st.updated_at))
        self.assertTrue(hasattr(st, "name"))


if __name__ == "__main__":
    unittest.main()
