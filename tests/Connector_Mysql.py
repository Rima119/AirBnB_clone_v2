import MySQLdb
"""
Test if we create a new state , it's saves to the record
"""

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db_states", charset="utf8")
cur = db.cursor()
cur.execute("USE db_states")
