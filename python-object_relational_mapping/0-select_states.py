#!/usr/bin/python3
"""
connect to database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)
    db.close()
