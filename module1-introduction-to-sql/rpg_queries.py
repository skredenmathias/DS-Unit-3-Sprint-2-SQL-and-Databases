import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')

# 1. How many total characters?
curs = conn.cursor()
curs.execute('SELECT count(*) FROM charactercreator_character;')
curs.fetchall()
curs.close()
# SELECT count(*)
# FROM charactercreator_character;

# 2. How many of each subclass?
curs2 = conn.cursor()
query = 'SELECT count(*) FROM charactercreator_cleric;'

curs2.execute(query)
curs2.fetchall()
curs2.close()

curs2 = conn.cursor()
query = 'SELECT count(*) FROM charactercreator_fighter;'
curs2.execute(query)
curs2.fetchall()
curs2.close()

curs2 = conn.cursor()
query = 'SELECT count(*) FROM charactercreator_mage;'
curs2.execute(query)
curs2.fetchall()
curs2.close()

curs2 = conn.cursor()
query = 'SELECT count(*) FROM charactercreator_necromancer;'
curs2.execute(query)
curs2.fetchall()
curs2.close()

curs2 = conn.cursor()
query = 'SELECT count(*) FROM charactercreator_thief;'
curs2.execute(query)
curs2.fetchall()
curs2.close()

# 3 How many total items?
curs3 = conn.cursor()
query = 'SELECT count(*) FROM armory_item;'
curs3.execute(query)
curs3.fetchall()
curs3.close()
# 4 How many are weapons? How many are not? (first 20 rows)

curs4 = conn.cursor() # could include count(*) in 1st line query
query = '''SELECT ai.item_id, aw.item_ptr_id
FROM armory_item AS ai,
armory_weapon as aw
WHERE ai.item_id = aw.item_ptr_id
LIMIT 20;'''
curs4.execute(query)
curs4.fetchall()
curs4.close()
# Alternatively, SELECT COUNT(item_ptr_id)

# Not:

curs5 = conn.cursor()
query = '''SELECT ai.item_id
FROM armory_item AS ai
LEFT JOIN armory_weapon ON item_ptr_id = ai.item_id
WHERE item_ptr_id IS NULL'''
curs5.execute(query)
curs5.fetchall()
curs5.close()

# 5 How many items per char? (first 20)
curs6 = conn.cursor()
query = '''SELECT cc.character_id AS character_id, cc.name, 
COUNT(ai.item_id) AS num_items
FROM charactercreator_character AS cc,
armory_item AS ai, 
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
GROUP BY cc.character_id
ORDER BY 3 DESC
LIMIT 20;'''
curs6.execute(query)
curs6.fetchall()
curs6.close()

# 6 How many weapons per character? (first 20)
curs7 = conn.cursor()
query = '''
SELECT cc.character_id AS character_id, cc.name, COUNT(aw.item_ptr_id) AS num_weapons
FROM charactercreator_character AS cc,
armory_item AS ai, 
armory_weapon AS aw,
charactercreator_character_inventory AS cci
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
AND ai.item_id = aw.item_ptr_id
GROUP BY cc.character_id
ORDER BY 3 DESC
LIMIT 20;'''
curs7.execute(query)
curs7.fetchall()
curs7.close()
#Chris ish
# SELECT cci.character_id, COUNT(cci.item_id)
# FROM charactercreator_character_inventory AS cci
# WHERE cci.item_id IN (SELECT item_ptr_id FROM armory_weapon)
# GROUP BY cci.character_id
# ORDER BY 2 DESC;

# 7 On avg, how many items per char?
curs8 = conn.cursor()
query = '''
SELECT CAST(COUNT(cci.item_id) AS Float)/CAST(COUNT(DISTINCT cci.character_id) AS Float)
FROM charactercreator_character_inventory cci'''
curs8.execute(query)
curs8.fetchall()
curs8.close()

# 8 On avg, how many weapons per char?
curs9 = conn.cursor()
query = '''
SELECT CAST(COUNT(cci.item_id) AS Float)/CAST(COUNT(DISTINCT cci.character_id) AS Float)
FROM charactercreator_character_inventory cci
WHERE cci.item_id IN (
SELECT aw.item_ptr_id
FROM armory_weapon aw);'''
curs9.execute(query)
curs9.fetchall()
curs9.close()