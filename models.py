from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime, timedelta


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
    

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    borrow_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    due_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)   # None یعنی هنوز پس نداده

    # Relationships
    user = relationship("User", backref="loans")
    book = relationship("Book", backref="loans")

    def __init__(self, user_id: int, book_id: int):
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = datetime.utcnow()
        self.due_date = self.borrow_date + timedelta(days=30)