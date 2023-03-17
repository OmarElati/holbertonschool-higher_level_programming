#!/usr/bin/python3
"""
connect to database and lists all states with a name starting with N (upper N)
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Open database connection
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states\
        WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    # Fetch all the rows using fetchall() method.
    data = cursor.fetchall()
    for row in data:
        print(row)
    db.close()
