import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('opened data successfully')


import pandas as pd
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table';""",conn)

#print(tables)
nd = pd.read_sql("""SELECT Season_Id, Match_Id,
                 v.Venue_Name, c.City_Name, t.Team_Name AS Winner
                 FROM Match
                 INNER JOIN Venue AS v ON
                 match.Venue_Id == v.Venue_Id
                 INNER JOIN City AS c ON v.City_Id == c.City_Id
                 INNER JOIN Team AS t ON
                 match.Match_Winner == t.Team_Id;""",conn)
#print(nd)
te = pd.read_sql("""SELECT * FROM Team""", conn)
print(te)

ma = pd.read_sql("""SELECT * FROM Match""", conn)
print(ma)

se = pd.read_sql("""SELECT * FROM Season""", conn)
print(se)

cm15 = pd.read_sql("""SELECT Match_Id, Team_2 as A_T, Toss_Winner, Match_Winner
                  FROM Match
                  WHERE Team_1 =
                  (SELECT Team_1
                  FROM Match
                  WHERE Team_1 == 3 AND Season_Id == 8)""", conn)
print(cm15)