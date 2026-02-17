'''
Please note:

The first file that you should run in this level is tests.py for database creation, with all tests passing.
Remember that running the hack.py will change the state of the database, causing some tests inside tests.py
to fail.

If you like to return to the initial state of the database, please delete the database (level-4.db) and run 
the tests.py again to recreate it.
'''

import sqlite3

# Please note: The following code is NOT expected to run and it's provided for explanation only

# Vulnerable: this code will allow an attacker to insert the "DROP TABLE" SQL command into the query
# and delete all users from the database.
con = sqlite3.connect('example.db')
user_input = "Mary'); DROP TABLE Users;--"
sql_stmt = "INSERT INTO Users (user) VALUES ('" + user_input + "');"
con.executescript(sql_stmt)

# Secure through Parameterized Statements
con = sqlite3.connect('example.db')
user_input = "Mary'); DROP TABLE Users;--"
# The secure way to query a database is
con.execute("INSERT INTO Users (user) VALUES (?)", (user_input,))
