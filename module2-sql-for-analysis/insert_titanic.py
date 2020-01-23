import psycopg2
import sqlite3
import pandas as pd

# Create empty sqlite3 database (Could be input later?)
sl_conn = sqlite3.connect('titanic.sqlite3')

# load in csv to pandas
df = pd.read_csv('titanic.csv')
print('pandas table:')
# print('df.head()')
print(df.shape)
# print(df.columns)
df['Name'] = df['Name'].str.replace(r"[\"\',]", '')

# Populate database
df.to_sql('titanic', sl_conn, if_exists='replace')

# Create a cursor
sl_curs = sl_conn.cursor()


# Step 1: Extract
# Grab values from table
get_values = 'SELECT * FROM titanic'
titanic_values = sl_curs.execute(get_values).fetchall()

# Consider:
print('PRAGMA (SQLite?) table:')
print(sl_curs.execute('PRAGMA table_info(titanic);').fetchall())


# Step 2: Transform

create_table_statement = '''
CREATE TABLE titanic(
    index SERIAL PRIMARY KEY,
    Survived INT NOT NULL,
    Pclass INT,
    Name VARCHAR(85),
    Sex TEXT,
    Age REAL,
    Siblings_Spouse INT,
    Parents_Children INT,
    Fare REAL
);
'''

# Access ElephantSQL database
dbname = 'jzdtgbzn'
user = 'jzdtgbzn'
password = 'cw63FpnYdYoEO4Ih1WNiDLdCPXadK0RP'
host = 'balarama.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Open postgres cursor
pg_curs = pg_conn.cursor()

# Create our table in pg
pg_curs.execute("DROP TABLE IF EXISTS titanic")
pg_curs.execute(create_table_statement)
pg_conn.commit()

# Mystery code
show_tables = '''
SELECT
    *
FROM
    pg_catalog.pg_tables
WHERE
    schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
'''
pg_curs.execute(show_tables)
print('postgreSQL table:')
print(pg_curs.fetchall())


# Step ? Populate:
for person in titanic_values:
    insert_statement = '''
        INSERT INTO titanic (Survived, Pclass, Name, Sex, Age, 
        Siblings_Spouse, Parents_Children, Fare) 
        VALUES ''' + str(person[1:]) + ';'
    pg_curs.execute(insert_statement)
pg_conn.commit()


# Test
pg_curs.execute('SELECT * FROM titanic')
pg_titanic = pg_curs.fetchall()

# for person, pg_person in zip(titanic_values, pg_titanic):
#     assert person == pg_person
# print(type(pg_titanic))
# print(pg_titanic[:5])

# Survived:
'''
SELECT count(Survived)
FROM titanic
WHERE Survived=1;
'''

# Died:
'''
SELECT count(Survived)
FROM titanic
WHERE Survived=1;
'''

# How many passengers in each class?
'''
SELECT Pclass, count(Name)
from titanic
GROUP BY Pclass;
'''

# How many survived / died within each class?
'''
SELECT Pclass, Survived, count(*)
from titanic
GROUP BY Pclass, Survived
ORDER BY Pclass, Survived;
'''
# What was the average age of survivors vs nonsurvivors?
'''
SELECT avg(Age), Survived
from titanic
GROUP BY Survived
'''
# ALSO CASE:
'''
SELECT avg(Age) || (CASE WHEN Survived = 1 THEN
' avg age of survivors' ELSE ' avg age of nonsurvivors'
END)
from titanic
GROUP BY Survived
'''

# What was the average age of each passenger class?
'''
SELECT Age, Pclass
FROM titanic
GROUP BY Pclass
'''

# What was the average fare by passenger class? By survival?
'''
SELECT Pclass, Fare, Survived
from titanic
group by Pclass, Survived;
'''

# How many siblings/spouses aboard on average, by passenger class? By survival?
'''

'''