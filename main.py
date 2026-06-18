from database import Base , engine , SessionLocal
from crud import create_book
from models import Book
from auth import main_auth


def run():
    
    print("welcome to markazi library")
    Base.metadata.create_all(bind=engine)
    main_auth()

    
if __name__ == "__main__":
    run()