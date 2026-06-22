import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('opened data successfully')


import pandas as pd
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table';""",conn)

print(tables)
jc = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                 FROM country c
                 INNER JOIN city ci
                 ON c.Country_Id == ci.Country_id""",conn)
print(jc)

jl = pd.read_sql("""SELECT *
                 FROM player p
                 LEFT JOIN season s
                 ON p.Player_Id == s.Man_of_the_Series """,conn)
print(jl)
joc =  pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                 FROM country c
                 CROSS JOIN city ci""",conn)
print(joc)

u =  pd.read_sql("""SELECT Player_Name
                 FROM player
                 UNION
                 SELECT Team_Name
                 FROM team""",conn)
print(u)