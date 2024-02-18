#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument and safe from MySQL injections
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    input_arg = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            port=3306)

    cur = db.cursor()
    query = "SELECT * FROM states\
        WHERE name LIKE BINARY %s\
        ORDER BY id ASC"
    cur.execute(query, (input_arg,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
