#from _typeshed import ReadableBuffer
from re import MULTILINE
from unittest import result
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
from difflib import SequenceMatcher
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
     scores={}
     for role in roles:
         doc=list ( Roles_collection.find({"_id":role}))
         role_name=doc[0]['role_name']
         role_equivalents=doc[0].get('role_equivalent_terms', [])
         role_equivalent_jobtitle=doc[0].get('role_equivalent_jobTitle', [])
         if (role_name==Job_title ):
             role_core_competencies=[]
             role_secondary_competencies=[]
             for competency in doc[0]['role_core_competencies']:
                 core_competency_doc =list ( Competencies_collection.find({"_id":competency}))
                 role_core_competencies.append(core_competency_doc[0])
             for competency in doc[0]['role_secondary_competencies']:
                 secondary_competency_doc =list ( Competencies_collection.find({"_id":competency}))
                 role_secondary_competencies.append(secondary_competency_doc[0])
            
             doc[0]['role_core_competencies']= role_core_competencies
             doc[0]['role_secondary_competencies']=role_secondary_competencies
             scores['10']=doc[0]
         else:
             for role in role_equivalent_jobtitle:
                if SequenceMatcher(None, role_name, role).ratio()>0.7 :
                    role_core_competencies=[]
                    role_secondary_competencies=[]
                    for competency in doc[0]['role_core_competencies']:
                       core_competency_doc =list ( Competencies_collection.find({"_id":competency}))
                       role_core_competencies.append(core_competency_doc[0])
                    for competency in doc[0]['role_secondary_competencies']:
                       secondary_competency_doc =list ( Competencies_collection.find({"_id":competency}))
                       role_secondary_competencies.append(secondary_competency_doc[0])
            
                    doc[0]['role_core_competencies']= role_core_competencies
                    doc[0]['role_secondary_competencies']=role_secondary_competencies
                    scores['8']=doc[0]
                    break
             for equivalent_role in role_equivalents :
                 if SequenceMatcher(None, role_name, equivalent_role).ratio()>0.7:
                    role_core_competencies=[]
                    role_secondary_competencies=[]
                    for competency in doc[0]['role_core_competencies']:
                       core_competency_doc =list ( Competencies_collection.find({"_id":competency}))
                       role_core_competencies.append(core_competency_doc[0])
                    for competency in doc[0]['role_secondary_competencies']:
                       secondary_competency_doc =list ( Competencies_collection.find({"_id":competency}))
                       role_secondary_competencies.append(secondary_competency_doc[0])
            
                    doc[0]['role_core_competencies']= role_core_competencies
                    doc[0]['role_secondary_competencies']=role_secondary_competencies
                    scores['5']=doc[0]
     scores=dict(sorted(scores.items()))
     for i in scores.keys():
         data.append(scores[i])
     
             
     
     
     return ResponseModel_get(data, "Roles retrieved successfully")
    
