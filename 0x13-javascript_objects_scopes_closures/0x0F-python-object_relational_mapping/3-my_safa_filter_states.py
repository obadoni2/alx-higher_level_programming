#!/usr/bin/python3
'''
script that takes in an argument amd displays all values
'''
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.Connect(
        usr=sys.argv[1],
        passwd=sys.argv[2],
        db= sys.argv[3],
        port=3306,
        host='localhost')
    cursor =db.cursor()
    cursor.execute('SELECT * from states WHERE name =%s ORDER BY state.id,
                   (sys.argv[4],)')
    
    states = cursor.fetchall()
    for state in states:
        print(states)
        
    cursor.close()
    db.close()
    
        
         
                       
    