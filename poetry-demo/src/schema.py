from enum import Enum
from sqlalchemy import orm
from sqlalchemy.sql.base import NO_ARG
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.functions import user
from pydantic import BaseModel, Field
from typing import Optional
from .models import GenderEnum
from sqlalchemy import Enum
import enum

class UserBase(BaseModel):
    fname: Optional [str] = None
    lname: Optional [str] = None
    class Config:
        # schema_extra = {
        #     "example": {
        #         "fname":"",
        #         "lname":"",
        #         "gender":"",
        #     }
        # }
        orm_mode = True

        use_enum_values = True


class UserCreate(UserBase):
    fname : str
    lname : str




class User(UserBase):
    id : int

class UserUpdate(UserBase):
    pass
