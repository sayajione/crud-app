from typing import List
from sqlalchemy import Column, String, Integer, Enum
from src.database import Base
import enum


class GenderEnum(str, enum.Enum):
    male = "male"
    female = "female"

class User(Base):
    __tablename__ = "users" 
    id = Column(Integer,primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    gender = Column(Enum(GenderEnum))

# class ModelUser(User, GenderEnum):
#     pass

# pydantic config
# configure docker



