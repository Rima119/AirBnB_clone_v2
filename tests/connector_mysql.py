#!/usr/bin/python3
import MySQLdb
import os

db = MySQLdb.connect(host="localhost", port=3306, 
        user="root", passwd="root", db=os.environ.get('DB_test'))
cur = db.cursor()
