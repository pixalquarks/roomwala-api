from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Body
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from . import models, utils
from .database import engine
from .routers import owner, auth, flats

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"] 
)

app.include_router(owner.router)
app.include_router(auth.router)
app.include_router(flats.router)

@app.get("/")
def home():
    return {"message" : "Hello, World!!!"}



    