from datetime import datetime
from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.sqltypes import TIMESTAMP
from typing import Optional, List

# from app.models import Owner


class Owner(BaseModel):
    name : str
    mobile : str
    email : EmailStr
    password : str
    
class OwnerOut(BaseModel):
    id : int
    name : str
    mobile : str
    email : EmailStr
    activated : int
    created_at : datetime
    
    class Config:
        orm_mode = True
    
class OwnerLogin(BaseModel):
    email : EmailStr
    password : str
    
    
class Token(BaseModel):
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    id : int = None
    
class Flat(BaseModel):
    address : str
    price : int
    bhk : int
    images : str = ""
    saxx_preference : int = 0
    furnishing : int = 0
    electricity : int = 0
    water : int = 0
    locality : str
    description : str
    
class FlatOut(Flat):
    owner : OwnerOut
    
    class Config:
        orm_mode = True


class EmailSchema(BaseModel):
    email : List[EmailStr]