from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session, raiseload
import src.models as models
import src.schema as schema
from src.database import get_db, engine
from fastapi.encoders import jsonable_encoder


def userinfo(db):
    return db.query(models.User).all()


def createuser(user,gender_type, db):
    if gender_type.value ==  'male':
        choosen_gender = "male"
    else:
        choosen_gender = "female"
    db_user = models.User(fname=user.fname, lname=user.lname, gender = choosen_gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def updateuser(id, user, db):
    user_data = db.query(models.User).filter(models.User.id == id).first()
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with {id} not found')
    json_data = jsonable_encoder(user_data)
    new_data = user.dict(exclude_unset=True)
    for field in json_data:
        if field in new_data != None:
            setattr(user_data, field, new_data[field])
    db.commit()
    db.refresh(user_data)
    return user_data



def deleteuser(id: int, db: Session = Depends(get_db)):
    db.query(models.User).filter(models.User.id ==
                                 id).delete(synchronize_session=False)
    db.commit()
    return f'User with id: {id} deleted successfully'
