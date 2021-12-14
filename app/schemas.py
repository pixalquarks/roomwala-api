from datetime import datetime
from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.sqltypes import TIMESTAMP
from typing import Optional

from app.models import Owner


class User(BaseModel):
    name : str
    mobile : str
    email : EmailStr
    password : str
    
class UserOut(BaseModel):
    id : int
    name : str
    mobile : str
    email : EmailStr
    created_at : datetime
    
    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    email : EmailStr
    password : str
    
    
class Token(BaseModel):
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    id : int = None
    name : str
    
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
    owner : UserOut
    
    class Config:
        orm_mode = True