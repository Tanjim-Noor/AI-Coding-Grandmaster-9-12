# Activity 1: Let's join tables

# Import Dataset
from google.colab import files
uploaded = files.upload()

# Import Necessary Libraries
import numpy as np
import pandas as pd
import sqlite3

# Setup connection with database and display all tables
database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table'""", conn)
print(tables)

# Check how Inner join works
joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                            FROM country c
                            INNER JOIN city ci
                            ON c.Country_Id == ci.Country_id""", conn)
print('Inner Join Result:')
print(joined_city)

# Check how Left join works
joined_left = pd.read_sql("""SELECT *
                            FROM player
                            LEFT JOIN season
                            ON player.Player_Id == season.Man_of_the_Series""", conn)
print('Left Join Result:')
print(joined_left)

# Check how Cross join works
joined_cross = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                            FROM country c
                            CROSS JOIN city ci""", conn)
print('Cross Join Result:')
print(joined_cross)

# Check how Union Clause works
union = pd.read_sql("""SELECT Player_Name 
                      FROM player
                      UNION
                      SELECT Team_Name
                      FROM team""", conn)
print('Union Result:')
print(union)

conn.close()
