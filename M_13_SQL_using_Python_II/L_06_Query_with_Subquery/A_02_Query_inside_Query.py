# Activity 2: Query inside Query

# Import Dataset
from google.colab import files
uploaded = files.upload()

# Import necessary libraries
import pandas as pd
import numpy as np
from datetime import datetime
import sqlite3

# Setup connection and show tables
database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
print(tables)

# Example query with subquery
player_best = pd.read_sql("""SELECT * FROM Player_Match
                          WHERE Player_Id IN (
                              SELECT Player_Id FROM Player_Match
                              GROUP BY Player_Id
                              HAVING SUM(Runs_Scored) > 500
                          );""", conn)
print(player_best)

conn.close()
