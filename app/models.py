from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
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

    
class Flat(Base):
    __tablename__ = "flats"
    
    id = Column(Integer, primary_key=True, nullable=False)
    address = Column(String(100), nullable=False) 
    price = Column(Integer, nullable=False)
    bhk = Column(Integer, nullable=False)
    # furnishing = Column(Enum(FurnishEnum), nullable=False)
    locality = Column(String(20), nullable=False)
    
    images = Column(String(250))
    saxx_preference = Column(Integer)
    furnishing = Column(Integer)
    electricity = Column(Integer)
    water = Column(Integer)
    
    description = Column(String(300), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    
    owner_id = Column(Integer, ForeignKey("owners.id", ondelete="CASCADE"), nullable=False)
    
    owner = relationship("Owner")
