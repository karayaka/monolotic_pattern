from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL="postgresql://admin:55315531@localhost:5432/fastapiDb"

engine= create_engine(DATABASE_URL)

SesionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    try:
        db=SesionLocal()
        yield db
    finally:
        db.close()