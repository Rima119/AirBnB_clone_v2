#!/usr/bin/python3
"""unittests for models/engine/db_storage.py"""
import unittest
import pep8
import json
import os
import inspect
import MySQLdb
from models.user import User
from models.base_model import BaseModel, Base
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class TestDBStorage(unittest.TestCase):
    """Unittests for testing the DBStorage"""

    @classmethod
    def setUpClass(cls):
        """set up"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_DBStorage(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        d = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(d.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)


if __name__ == "__main__":
    unittest.main()
