from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo

app = Flask(__name__)
app.config.from_object(Config)
client = pymongo.MongoClient("mongodb+srv://cireyennek:r4W3fXCuwxBhVDgkqXpg@cluster0-hotkd.mongodb.net/test?retryWrites=true&w=majority")
db = client["Cluster0-sandbox"]
col = db['openings']
openings = list(col.find())

from app import routes, models
