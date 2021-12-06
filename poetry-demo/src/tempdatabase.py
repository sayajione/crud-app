from abc import get_cache_token
import enum
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
import sqlalchemy.pool as pool
import psycopg2
from config import cnf
from sqlalchemy.ext.declarative import declarative_base
hostname = cnf.HOST.get_secret_value()
user = cnf.USER.get_secret_value()
port = cnf.PORT.get_secret_value()
pwd = cnf.PASSWORD.get_secret_value()
# func for creating connection string
def getconn():
    SQL_CONNECTION_STRING =   psycopg2.connect(username = {user}, host = {hostname}, dbname = 'user')
    return SQL_CONNECTION_STRING

mypool = pool.QueuePool(create_engine = getconn, pool_size=5 , max_overflow= 15)
 
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