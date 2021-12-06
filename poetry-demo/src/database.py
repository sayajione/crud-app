# import dotenv
# from dotenv.main import dotenv_values
# from pydantic.fields import Field
# from pydantic.types import condecimal
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# from config import cnf
# from sqlalchemy.orm.session import Session
# import os



# # user = os.environ.get('user')
# # pwd = os.environ.get('password')
# # host = os.environ.get('host')
# # port = os.environ.get('port')
# # print(user, pwd, host, port)
# user = cnf.USER.get_secret_value()
# pwd = cnf.PASSWORD.get_secret_value()
# host = cnf.HOST.get_secret_value()
# port = cnf.PORT.get_secret_value()
# # print(user, pwd, host, port)

# # SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/user"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
# # creating a session 
# # also binding the engine to session maker
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     # db is an object of session    
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# -----------------------------------------------------------------------------------------
# testing sqlalchemy pooling 
# -----------------------------------------------------------------------------------------
from abc import get_cache_token
import enum
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
import sqlalchemy.pool as pool
import psycopg2
from config import cnf
from sqlalchemy.ext.declarative import declarative_base
# hostname = cnf.HOST.get_secret_value()
# user = cnf.USER.get_secret_value()
# port = cnf.PORT.get_secret_value()
# pwd = cnf.PASSWORD.get_secret_value()
# func for creating connection string
def getconn():
    SQL_CONNECTION_STRING =   psycopg2.connect(user = 'testuser', password = 'demouser', host='localhost', port = 3306, dbname='user', sslmode = "disable")
    return SQL_CONNECTION_STRING


mypool = pool.QueuePool(creator = getconn, pool_size=5 , max_overflow= 15)
 
engine = create_engine('mysql+mysqlconnector://',pool= mypool)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    # db is an object of session    
    db = session()
    try:
        yield db
    finally:
        db.close()