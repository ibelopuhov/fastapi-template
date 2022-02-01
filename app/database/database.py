from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.api.settings import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@ \
                          {settings.database_hostname}:{str(settings.database_port)}/{settings.database_name}'

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf-8')

SessionLocal: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db: sessionmaker = SessionLocal()
    try:
        yield db
    finally:
        db.close()
