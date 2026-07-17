from sqlalchemy.orm import Session
from models import Book , User
from sqlalchemy import or_
from models import Loan
from datetime import datetime

# ==================== BOOK FUNCTIONS ====================

def create_book(db: Session, title: str , author: str):
    
    book = Book(title=title , author=author )
    
    db.add(book)
    db.commit()
    db.refresh(book)

    return book

# Check if book already exists
def check_isbn(db: Session, isbn: str):
    return db.query(Book).filter(Book.isbn == isbn).first() is not None


def get_book(db: Session, book_id: int):
    """Get a single book by ID"""
    return db.query(Book).filter(Book.id == book_id).first()


def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    """List all books with pagination"""
    return db.query(Book).offset(skip).limit(limit).all()


def search_books(db: Session, query: str):
    """Search books by title, author, or isbn"""
    return db.query(Book).filter(
        or_(
            Book.title.ilike(f"%{query}%"),
            Book.author.ilike(f"%{query}%"),
            Book.isbn.ilike(f"%{query}%"),
            Book.id.ilike(f"%{query}%")
        )
    ).all()


def update_book(db: Session, book_id: int, title: str = None, author: str = None, isbn: str = None):
    """Update book information"""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    
    if title is not None:
        book.title = title
    if author is not None:
        book.author = author
    if isbn is not None:
        book.isbn = isbn
    
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, query):
    """Delete a book by ID """

    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return False
    
    db.delete(book)
    db.commit()
    return True

def borrow_book(db: Session, user_id: int, book_id: int):
    """Borrow a book"""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return False, "Book not found"

    active_loan = db.query(Loan).filter(Loan.book_id == book_id, Loan.return_date == None).first()
    if active_loan:
        return False, "This book is already borrowed"

    loan = Loan(user_id=user_id, book_id=book_id)
    db.add(loan)
    db.commit()
    db.refresh(loan)
    return True, f"Book'{book.title}' borrowed successfully. Due date:{loan.due_date.date()}"


def return_book(db: Session, user_id: int, loan_id: int):
    """Return a book"""
    loan = db.query(Loan).filter(Loan.id == loan_id, Loan.user_id == user_id, Loan.return_date == None).first()
    if not loan:
        return False, "No active loan found for this book"

    loan.return_date = datetime.utcnow()
    db.commit()
    return True, f"Book'{loan.book.title}' returned successfully"




# ==================== USER FUNCTIONS ====================

def check_username(db: Session, username: str) -> bool:
    user = db.query(User).filter(User.username == username).first()
    return user is not None

def check_phonenumber(db: Session, phone: str) -> bool:
    user = db.query(User).filter(User.phonenumber == phone).first()
    return user is not None

def create_user(db: Session, username: str, password: str, phonenumber: str):

    user = User(
        username=username,
        password=password,        # TODO: Hash password later with bcrypt
        phonenumber=phonenumber,
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

def get_user_loans(db: Session, user_id: int):
    """دریافت لیست قرض‌های کاربر"""
    return db.query(Loan).filter(Loan.user_id == user_id).all()


