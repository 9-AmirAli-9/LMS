from sqlalchemy import Column , String , Integer , Boolean
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer , autoincrement=1 , primary_key=True )
    title = Column(String(100) , nullable=True , default="Unknown book name")
    authur = Column(String(100) , nullable=True , default="Unknown book authur")
    genre = Column(String(100) , nullable=True , default="Unknown book genre")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True , autoincrement=1)
    username = Column(String(50) , nullable=True , default="Unknown")
    password = Column(String , nullable=False)
    phonenumber = Column(String(20) , nullable=True , default="0")
    is_admin = Column(Boolean , nullable=True , default = False)
    