import pandas as pd
import sqlite3

df = pd.read_csv('table_clean.csv')

connection = sqlite3.connect('website\website\db.sqlite3')

df.to_sql('main_app_tc', connection, if_exists= 'replace')

connection.close()