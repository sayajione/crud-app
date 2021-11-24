from types import resolve_bases
from sqlalchemy.sql.functions import mode

from sqlalchemy.sql.sqltypes import DECIMAL
from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
import src.models as models
import src.schema as schema
from . import crud
from src.database import get_db, engine
from typing import List
from fastapi.encoders import jsonable_encoder

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


@router.get("/users")
def read_user(db : Session = Depends(get_db)):
    users = crud.userinfo(db = db)
    return users


@router.post("/createuser", response_model=schema.UserBase)
def createuser(user : schema.UserCreate, gender_type : models.GenderEnum, db : Session = Depends(get_db)):
    return crud.createuser(user=user, gender_type = gender_type, db = db )



@router.put("/updateuser/{id}", response_model = schema.UserUpdate)
def updateuser(id : int, user : schema.UserUpdate, db : Session  = Depends(get_db)):
    return crud.updateuser(id = id, user = user, db = db)


@router.delete("/deleteuser/{id}")
def deleteuser(id : int ,db : Session = Depends(get_db)):
    return crud.deleteuser(id = id , db = db)
