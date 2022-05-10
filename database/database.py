from pymongo.mongo_client import MongoClient
import motor.motor_asyncio
from bson import ObjectId
from pydantic.networks import EmailStr
import ssl
import pymongo 
from models import  * 

dev = 'mongodb+srv://Rania_Hamdeni:careerboosts2000@cluster0.vfuyb.mongodb.net/test?authSource=admin&replicaSet=atlas-12sscv-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
client = pymongo.MongoClient(dev, ssl=True)
database = client['Skills-Framework']

Roles_collection = database.get_collection('Roles')
Competencies_collection = database.get_collection('Competencies')
Frameworks_collection = database.get_collection('Frameworks')






   
   









