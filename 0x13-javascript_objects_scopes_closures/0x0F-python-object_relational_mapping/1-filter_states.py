#!/usr/bin/python3
'''
lists all states with a name starting with N
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user = sys.argv[1],
        passwd = sys.argv[2],
        db=sys.argv[3],
        port = 3306,
        host= 'localhost')
    
    cursor = db.cursor()
    cursor.execute("SELECT *\
                    FROM states \
                    WHERE CONVERT(`name` USING latin1) \
                    COLLATE latin1_general_CS \
                    LIKE 'N%';")
    
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
    