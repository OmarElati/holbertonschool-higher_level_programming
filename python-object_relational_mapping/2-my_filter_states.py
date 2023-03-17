#!/usr/bin/python3
"""
    Script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                   .format(state_name))

    # Fetch a single row using fetchone() method.
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # disconnect from server
    cursor.close()
    db.close()
