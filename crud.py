from sqlalchemy.orm import Session
from models import Book , User

# ==================== BOOK FUNCTIONS ====================

def create_book(db: Session, title: str , authur: str, genre: str):
    
    book = Book(title=title , authur=authur , genre=genre)
    
    db.add(book)
    db.commit()
    db.refresh()

    return book


# ==================== USER FUNCTIONS ====================

def check_username(db: Session, username: str) -> bool:
    user = db.query(User).filter(User.username == username).first()
    return user is not None

def check_phonenumber(db: Session, phone: str) -> bool:
    user = db.query(User).filter(User.phonenumber == phone).first()
    return user is not None

def create_user(db: Session, username: str, password: str, phonenumber: str, is_admin: bool = False):

    user = User(
        username=username,
        password=password,        # TODO: Hash password later with bcrypt
        phonenumber=phonenumber,
        is_admin=is_admin
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def authenticate_user(db: Session, username: str, password: str):

    user = db.query(User).filter(User.username == username).first()
    if user and user.password == password:   # TODO: Use password hashing later
        return user
    return None