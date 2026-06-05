import sqlite3

basketball = 'basketball.sqlite'

conn = sqlite3.connect(basketball)
print('opened data successfully')


import pandas as pd
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table';""",conn)
print(tables)