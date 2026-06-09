import sqlite3

database = 'database.sqlite'

con = sqlite3.connect(database)

import pandas as pd
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type = 'table';""",con)

print(tables)

matches = pd.read_sql("""SELECT *
                      FROM Match ;""",con)
print(matches)

winer = pd.read_sql("""SELECT *
                      FROM Match 
                     WHERE Match_Winner = 7;""",con)
print(winer)

minmax = pd.read_sql("""SELECT MIN(Win_Margin),
                      MAX(Win_Margin)
                      FROM Match  ;""",con)
print(minmax)