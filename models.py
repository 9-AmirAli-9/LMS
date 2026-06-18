from sqlalchemy import Column , String , Integer , Boolean
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer , autoincrement=True , primary_key=True )
    title = Column(String(100) , nullable=True , default="Unknown book name")
    author = Column(String(100) , nullable=True , default="Unknown book authur")
    isbn = Column(String(20), unique=True, nullable=True)
    

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True , autoincrement=True)
    username = Column(String(50) , nullable=True , default="Unknown")
    password = Column(String(50) , nullable=False)
    phonenumber = Column(String(20) , nullable=True , default="0")
    is_admin = Column(Boolean , nullable=True , default = False)
    