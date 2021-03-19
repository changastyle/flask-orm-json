from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
import pymysql 
from sqlalchemy.ext.declarative import declarative_base

host = "localhost"         
user = "root"          
passwd = "descargar"    
database = "chota"     

# Database connection
dbc=pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=database,
        autocommit=True)

engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}/{database}')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)