#!/usr/bin/python3
"""
list all states from the database btn_0e_0_usa

"""
import sys
import MySQLdb

if __name__ == '__main__':
    db =MySQLdb.Connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port = 3306,
        host = 'localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    
    states =  cursor.fetchall()
    for state in states:
        print(state)
    

    

    