from database import Base , engine , SessionLocal
from crud import create_book
from models import Book
import auth


def run():
    
    print("welcome to markazi library")

    auth()

    