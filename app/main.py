from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.params import Body
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from . import schemas, models, utils
from .database import engine
from .routers import owner, auth
# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
# )

# print(mydb)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(owner.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message" : "Hello, World!!!"}



    