import pandas as pd
import sqlite3

df = pd.read_csv('table_clean.csv')
df.to_csv('table_clean.csv', index=False)

db = pd.read_csv('table_clean.csv')

connection = sqlite3.connect('website\website\db.sqlite3')

db.to_sql('main_app_tc', connection, if_exists= 'replace', index=False)

connection.close()