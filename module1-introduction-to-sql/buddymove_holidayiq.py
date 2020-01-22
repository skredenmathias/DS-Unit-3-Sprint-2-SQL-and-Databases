import pandas as pd
import sqlite3

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)

df.to_sql('review', conn, if_exists='replace')

curs = conn.cursor()
curs.execute('SELECT COUNT(*) FROM review')
# curs.commit()
print('total rows:')
print(curs.fetchall()[0][0])
curs.close()

curs = conn.cursor()
query = '''
SELECT COUNT(*)