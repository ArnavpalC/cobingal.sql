import sqlite3

con = sqlite3.connect('database.sqlite')
print('opened data succesfully')

con.execute('''CREATE TABLE CLASS_11
             (SNO INT PRIMARY KEY NOT NULL,
             Roll_No INT NOT NULL,
             Name TEXT NOT NULL,
             AGE INT DEFAULT(15),
             GENDER TEXT NOT NULL,
             Email_ID TEXT NOT NULL,
             Contact_No REAL NOT NULL);''')

print('table created succesfully')

con.execute("INSERT INTO CLASS_11 (SNO, Roll_NO,NAME,AGE,Gender,Email_ID,Contact_no) \
       VALUES (1,1,'ALLEN',14,'Male','allen@gmail.com',8080900)");

con.execute("INSERT INTO CLASS_11 (SNO, Roll_NO,NAME,AGE,Gender,Email_ID,Contact_no) \
       VALUES (21,2,'Aisha',14,'Female','aish@gmail.com',9080900)");

con.execute("INSERT INTO CLASS_11 (SNO, Roll_NO,NAME,AGE,Gender,Email_ID,Contact_no) \
       VALUES (3,3,'Jeff',15,'Male','jeffen@gmail.com',9900900)");

con.commit()
print('records created successfully')

import pandas as pd
tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""", con)

print(tables)

class_11 = pd.read_sql("""SELECT *
                       FROM CLASS_11;""",con)

print(class_11.head())