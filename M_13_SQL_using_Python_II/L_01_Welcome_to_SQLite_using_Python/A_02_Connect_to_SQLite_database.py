# Activity 2: Connect to SQLite database
# Short description:
# Write a program to connect with the given SQLite database and print all the tables present inside the database.

import sqlite3
import pandas as pd

# Adjust this path if your database file is somewhere else.
DATABASE_FILE = 'database.sqlite'

try:
    conn = sqlite3.connect(DATABASE_FILE)
    print('Opened data successfully')

    # Read SQL query for getting all tables of database into a dataframe
    tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
    print('\nTables in database:')
    print(tables)

    # Read table from the database into dataframe
    matches = pd.read_sql("""SELECT * FROM Match;""", conn)
    print('\nMatches table info:')
    print(matches.head())

    print('\nMatch table columns:')
    print(matches.columns)

except Exception as e:
    print('Error connecting to SQLite:', e)
finally:
    conn.close()
