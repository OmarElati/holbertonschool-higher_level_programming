#!/usr/bin/python3
"""
Connect to a MySQL server and safely fetch data
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

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Execute the query using the execute() method
    cursor.execute("SELECT * FROM states WHERE\
                   name = %s ORDER BY id ASC", (argv[4],))

    # Fetch all the rows using fetchall() method
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
