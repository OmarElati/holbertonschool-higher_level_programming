#!/usr/bin/python3
"""
Connect to database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()

    for row in data:
        print(row)

    db.close()
