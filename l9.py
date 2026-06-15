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
rs1 = pd.read_sql("""SELECT AVG(Win_Margin),Match_Winner
                  FROM Match
                  WHERE Season_Id == 9
                  GROUP BY Match_Winner
                  ORDER BY AVG(Win_Margin);""",con)
print(rs1)

rs2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_Id)
                  FROM Match
                  WHERE Season_Id == 9;""",con)
print(rs2)
rs3 = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin),
                  AVG(Win_Margin), COUNT(DISTINCT(Man_of_the_Match))
                  FROM Match;""",con)
print(rs3)

rs4 = pd.read_sql("""SELECT SUM(Win_Margin)
                  FROM Match
                  WHERE Season_Id == 9;""", con)
print(rs4)