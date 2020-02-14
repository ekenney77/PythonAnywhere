from mongoengine.document import Document
from mongoengine.fields import DateTimeField, IntField, StringField, URLField
import pymongo
from app import db

class Post(Document):
    company = StringField(required=True)
    date = StringField(required=True)
    link = URLField(required=True)
    job_id = StringField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    teaser_text = StringField(required=True)
