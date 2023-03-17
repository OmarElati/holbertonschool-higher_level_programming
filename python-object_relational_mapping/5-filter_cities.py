#!/usr/bin/python3
"""
    Script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Open database connection
    db = MySQLdb.connect(user=mysql_username, passwd=mysql_password, db=db_name, port=3306, host='localhost')

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all rows and print them separated by commas
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    # Close database connection
    db.close()
