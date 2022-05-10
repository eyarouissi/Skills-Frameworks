#from _typeshed import ReadableBuffer
from re import MULTILINE
import pydantic
from bson import ObjectId
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
from fastapi import APIRouter, Body,  Request
from fastapi.encoders import jsonable_encoder
import pymongo
from starlette.routing import request_response 
from database.database import *
from models.Employee import *
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient
import  pymongo
router = APIRouter()


#Returns the roles
@router.get("/roles", response_description="roles retrieved")
async def get_roles(Job_title:str,framework:str):

    framework_doc = list ( Frameworks_collection.find({"framework_name":framework},{"framework_provider":0}))
    
    if framework_doc == [] :
     return ErrorResponseModel("An error occured.", 404, " The roles of this framework are not found")
    else :
     roles = framework_doc[0]['framework_roles']
     data=[]
     for role in roles:
         doc=list ( Roles_collection.find({"_id":role}))
         role_name=doc[0]['role_name']
         role_equivalents=doc[0].get('role_equivalent_terms', [])
         if (role_name==Job_title or Job_title in role_equivalents):
             data.append(doc[0])
             
     
     
     return ResponseModel_get(data, "Roles retrieved successfully")
    
