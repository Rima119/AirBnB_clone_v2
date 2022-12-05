import unittest
from models.state import State
from tests.test_models.Connector_Mysql import db, cur
"""Test_save_state_db: file what check if the State
object is saved"""


class test_save_state_db(unittest.TestCase):
    """Implemenation oh the save_state of the database"""
    def setUp(self):
        """Initialize the data"""
        self.State1 = State()
        self.State1.name = "California"

    def test_if_save_Object_state(self):
        """Check if Object is saved in db"""
        cur.execute("INSERT INTO stats VALUES (%s)", self.State1.name)
        self.assertGreater(cur.rowcount, 0)
        cur.close()
        db.close()
