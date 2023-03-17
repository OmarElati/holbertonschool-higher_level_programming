#!/usr/bin/python3
"""
connect to database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

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
    # Drop table if it already exist using execute() method.
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{:s}' \
    ORDER BY id ASC".format(argv[4]))
    data = cursor.fetchone()
    while (data):
        print(data)
        data = cursor.fetchone()
    cursor.close()
    db.close()
