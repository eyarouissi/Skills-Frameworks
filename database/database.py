from pymongo.mongo_client import MongoClient
import motor.motor_asyncio
from bson import ObjectId
from pydantic.networks import EmailStr
import ssl
import pymongo 
import os
from models import  * 
from dotenv import load_dotenv

load_dotenv()

mongo_details = os.getenv('MONGO_DETAILS')
client = pymongo.MongoClient(mongo_details, ssl=True)
database = client['Skills-Framework']

Roles_collection = database.get_collection('Roles')
Competencies_collection = database.get_collection('Competencies')
Frameworks_collection = database.get_collection('Frameworks')






   
   









