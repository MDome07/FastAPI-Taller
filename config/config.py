from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

con="mysql+pymysql://root@localhost:3306/taller"

motorcon=create_engine(con,echo=True)

ls=sessionmaker(autocommit=False,autoflush=False,bind=motorcon)

crearbd=declarative_base()