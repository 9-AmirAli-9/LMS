from sqlalchemy.orm import Session
from models import Book

def create_book(db: Session, title: str , authur: str, genre: str):
    
    book = Book(title=title , authur=authur , genre=genre)
    
    db.add(book)
    db.commit()
    db.refresh()

    return book


def check_username(db: Session , username: str):
    pass