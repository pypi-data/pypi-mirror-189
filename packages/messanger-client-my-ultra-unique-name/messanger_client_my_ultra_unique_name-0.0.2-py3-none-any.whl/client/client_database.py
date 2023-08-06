from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import default_comparator

from datetime import datetime

from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///client_db.db3', echo=False)
BASE = declarative_base()


class Contact(BASE):
    __tablename__ = 'contact'
    id = Column('id', Integer, primary_key=True)
    owner_name = Column('owner_name', String)
    contact_name = Column('contact_name', String)


class MessageHistory(BASE):
    __tablename__ = 'message_history'
    id = Column('id', Integer, primary_key=True)
    from_user_name = Column('from_user_name', String)
    to_user_name = Column('to_user_name', String)
    message = Column('message', Text)
    date = Column('date', DateTime, default=datetime.now())


BASE.metadata.create_all(engine)
create_session = sessionmaker(bind=engine)
