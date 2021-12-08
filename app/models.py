from typing import Sequence
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class Owner(Base):
    __tablename__ = "owners"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), nullable=False)
    mobile = Column(String(10), nullable=False)
    email = Column(String(32), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    verified = Column(Integer, server_default=text('0'))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
