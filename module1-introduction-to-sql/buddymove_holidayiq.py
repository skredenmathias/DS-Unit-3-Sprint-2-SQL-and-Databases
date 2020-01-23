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
SELECT count(Nature), count(Shopping)
FROM review
WHERE Nature > 100 AND Shopping > 100;
'''
curs.execute(query)
print('users with > 100 reviews for Nature & Shopping:')
print(curs.fetchall()[0][0]) # ?
curs.close()

# Avg reviews per category?
curs = conn.cursor()
categories = df.columns[1:].tolist()

for category in categories:
    query = f'SELECT avg({category}) FROM review;'
    curs.execute(query)
    print(category)
    print(round(curs.fetchall()[0][0], 2)) # ?
curs.close()