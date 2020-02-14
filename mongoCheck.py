from pymongo import MongoClient
import requests

client = MongoClient("mongodb+srv://cireyennek:r4W3fXCuwxBhVDgkqXpg@cluster0-hotkd.mongodb.net/test?retryWrites=true&w=majority")
db = client["Cluster0-sandbox"]
col = db['openings']
openings = list(col.find())

for item in openings:
    if requests.get(item['Link']).status_code == 200:
        print('yes')
    else:
        db.openings.remove(item)
