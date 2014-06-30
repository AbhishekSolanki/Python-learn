#SQLite

import sqlite3 as sql

#DB Connection
database1 = sql.connect('test1.db')

#Cursor object to perform SQL queries on DB
db1_cursor = database1.cursor()

#SQL Command
cmd = 'CREATE TABLE users(username TEXT,password TEXT)'
cmd2 = 'INSERT INTO users(username,password) VALUES("testuser","testpassword")'
cmd3 = 'SELECT * FROM users'

#Executing sql command with cursor
db1_cursor.execute(cmd)
db1_cursor.execute(cmd2)
db1_cursor.execute(cmd3)

#Save DB with commit command
database1.commit()

#print the data in cursor
for i in db1_cursor:
    print i

