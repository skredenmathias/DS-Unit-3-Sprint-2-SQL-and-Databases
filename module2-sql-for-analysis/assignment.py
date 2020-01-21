pip install psycopg2-binary

import psycopg2

dbname = 'jzdtgbzn'
user = 'jzdtgbzn'
password = 'cw63FpnYdYoEO4Ih1WNiDLdCPXadK0RP'
host = 'balarama.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password,
                           host=host)

pg_curs = pg_conn.cursor()

create_table_statement = '''
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
'''

insert_statement = '''
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
'''

pg_curs.execute(create_table_statement)
pg_curs.execute(insert_statement)
pg_conn.commit()


query = "SELECT * FROM test_table;"
pg_curs.execute(query)
pg_curs.fetchall()

wget https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true
!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

import sqlite3
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

row_count = 'SELECT COUNT(*) FROM charactercreator_character'
sl_curs.execute(row_count).fetchall()

get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

# What was the old schema?
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

create_character_table = '''
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
   name VARCHAR(30),
   level INT,
   exp INT,
   hp INT,
   strength INT,
   intelligence INT,
   dexterity INT,
   wisdom INT
);
'''
pg_curs.execute(create_character_table)
pg_conn.commit()


show_tables = '''
SELECT
    *
FROM
    pg_catalog.pg_tables
WHERE
    scemaname != 'pg_catalog'
AND schemename != 'information_schema';
'''
pg_curs.execute(show_tables)
pg_curs.fetchall()

for character in characters:
  insert_character = '''
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES ''' + str(character[1:]) + ';'
  pg_curs.execute(insert_character)
pg_conn.commit()
pg_curs.execute('SELECT * FROM charactercreator_character')
pg_curs.fetchall()
pg_curs.close()