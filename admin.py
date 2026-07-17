from database import get_db   # We'll make sure this exists
from crud import check_isbn , create_book , delete_book , search_books
import checker as ch   # if needed later
from console import console, print_success, print_error, print_header , Prompt , print_bold , Confirm

def add_book():
    """Admin function to add a new book"""
    print_header("\n=== Add New Book ===")
    
    title = Prompt.ask("Enter book title: ").strip()
    author = Prompt.ask("Enter author name: ").strip()
    isbn = Prompt.ask("Enter ISBN (optional, press Enter to skip): ").strip() or None
    
    
    db = next(get_db())
    
    try:
        # Check if ISBN already exists
        if isbn and check_isbn(db, isbn):
            print_error("A book with this ISBN already exists!")
            db.close()
            return
        
        book = create_book(db, title, author, isbn)
        print_success(f"Book added successfully! ID: {book.id}")
        
    except Exception as e:
        print_error(f"Error adding book: {e}")
    finally:
        db.close()



def delete():
    """Admin function to delete a book"""
    print_header("\n=== Delete Book ===")
    query = Prompt.ask("Enter id for delete book:")

    db = next(get_db())
    try:
        if not query:
            return

        book = search_books(db , query)
        if not book:
            print_error("Book not found.")
            return 

        print_info(f"ID.{book.id} | {book.title} | {book.author} | {book.isbn}")

        if Confirm.ask("Are you sure to delete this book: "):
            book = delete_book(db , query)
            print_success("Book deleted successfully.")
        else:
            print_error("you cancel the proccess.")
            return
    except Exception as e:
        print_error(f"Error deleting book {e}")
    finally:
        db.close()

def update()
    print_header("\n=== Update Book ===")







def admin_menu():
    """Main admin dashboard"""
    while True:
        print_header("\n=== Admin Panel ===")
        print_bold("1. Add Book")
        print_bold("2. Update Books")
        print_bold("3. Delete Book")
        print_bold("4. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print_info("Returning to main menu...")
            break
        else:
            print_error("Invalid choice! Please try again.")