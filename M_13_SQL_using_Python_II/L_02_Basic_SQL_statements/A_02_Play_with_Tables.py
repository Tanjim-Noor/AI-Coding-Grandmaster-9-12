# Activity 2: Play with Tables
# Short description:
# You are part of the Data Analytics team of the Mavericks Cricket Team.
# For analysing the data of the Matches table, perform tasks using SQL.

import sqlite3
import pandas as pd

DATABASE_FILE = 'database.sqlite'

with sqlite3.connect(DATABASE_FILE) as conn:
    # Check team id of all teams
    teams = pd.read_sql("""SELECT * FROM Team;""", conn)
    print('Team table:')
    print(teams.head())

    # Check details of all matches won by Mumbai Indians (Team Id assumed 7)
    MI_wins = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner = 7;""", conn)
    print('\nMatches won by Mumbai Indians:')
    print(MI_wins.head())

    # Check details for seasons 8 and 9
    MI_S8_S9 = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner = 7 AND Season_Id IN (8, 9);""", conn)
    print('\nMI matches in Season 8 & 9:')
    print(MI_S8_S9.head())

    # Teams starting with 'De'
    new_teams = pd.read_sql("""SELECT * FROM Team WHERE Team_Name LIKE 'De%';""", conn)
    print('\nTeams starting with De:')
    print(new_teams)

    # Min and max win margin
    min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin) AS minWinMargin, MAX(Win_Margin) AS maxWinMargin FROM Match;""", conn)
    print('\nMin and max win margin:')
    print(min_max_margin)
