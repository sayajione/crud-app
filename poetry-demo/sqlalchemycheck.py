
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
from os import name
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.database import SessionLocal
 
Base = declarative_base()
 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
 
 
from sqlalchemy import create_engine
engine = create_engine('sqlite:///')
 
from sqlalchemy.orm import sessionmaker
 
# Construct a sessionmaker object
session = sessionmaker()
 
# Bind the sessionmaker to engine
session.configure(bind=engine)
 
# Create all the tables in the database which are
# defined by Base's subclasses such as User
Base.metadata.create_all(engine)


s = session()

sayaji = User(name = 'Sayaji')
s.add(sayaji)
s.commit()
print(sayaji.id, sayaji.name)


mary = User(name ='Marry')
s.add(mary)
s.commit()
print(mary.id, mary.name)

# print(mary.id)
# mary.name = 'Soniya'
# print(mary.name)
# s.query(User).filter(User.name == 'Soniya').one()  
mary.name = 'Soniya'
s.commit() 
s.query(User).filter(User.name == 'Soniya').one()  
