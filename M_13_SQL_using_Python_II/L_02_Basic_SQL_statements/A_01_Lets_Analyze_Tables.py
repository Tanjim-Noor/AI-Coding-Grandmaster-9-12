# Activity 1: Let's Analyze Tables
# Short description:
# Connect to a SQLite database and inspect tables for structure and basic checks.

import sqlite3
import pandas as pd

DATABASE_FILE = 'database.sqlite'

with sqlite3.connect(DATABASE_FILE) as conn:
    # Get list of tables
    tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
    print('Database tables:')
    print(tables)

    # Check table named Match exists and print first rows
    if 'Match' in tables['name'].values:
        matches = pd.read_sql("""SELECT * FROM Match;""", conn)
        print('\nMatch table preview:')
        print(matches.head())
        print('\nMatch info:')
        print(matches.info())

    if 'Team' in tables['name'].values:
        teams = pd.read_sql("""SELECT * FROM Team;""", conn)
        print('\nTeam table preview:')
        print(teams.head())
