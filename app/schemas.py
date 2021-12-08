from datetime import datetime
from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.sqltypes import TIMESTAMP
from typing import Optional


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
    id : Optional[str] = None
    name : str