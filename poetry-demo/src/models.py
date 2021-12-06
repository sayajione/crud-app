from typing import List
from sqlalchemy import Column, String, Integer, Enum
from src.database import Base
import enum
from pydantic import BaseSettings, SecretStr


class GenderEnum(str, enum.Enum):
    male = "male"
    female = "female"

class User(Base):
    __tablename__ = "users" 
    id = Column(Integer,primary_key=True, index=True)
    fname = Column(String(20))
    lname = Column(String(20))
    gender = Column(Enum(GenderEnum))

# class ModelUser(User, GenderEnum):
#     pass

# pydantic config
# configure docker



