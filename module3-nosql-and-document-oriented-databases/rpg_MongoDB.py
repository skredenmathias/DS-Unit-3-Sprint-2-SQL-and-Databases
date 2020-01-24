import pymongo
# import rpg_db.sqlite3 as characters
# Need to: create conn object like in titanic / buddymove.
# https://github.com/LambdaSchool/Django-RPG/blob/master/testdata.json

mongo_pw = 'skreden'
ip = '46.230.129.54'

client = pymongo.MongoClient("mongodb://mathias:<passord123>@cluster0-shard-00-00-aklkr.mongodb.net:27017,cluster0-shard-00-01-aklkr.mongodb.net:27017,cluster0-shard-00-02-aklkr.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db.test)

for character in characters:
    rpg_doc = {
        'sql_key': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
        }
    db.test.insert_one(rpg.doc)