#!/usr/bin/python3
"""
Lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connects to a database to retrieve state values
    """

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("""SELECT * FROM states
                    WHERE states.name LIKE BINARY 'N%'
                    ORDER BY states.id ASC
                    """)
    rows = cur.fetchall()

    for row in rows:
        print(row)