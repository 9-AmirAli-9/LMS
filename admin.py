from database import get_db   # We'll make sure this exists
from crud import check_isbn , create_book
import checker as ch   # if needed later
from console import console, print_success, print_error, print_header , Prompt , print_bold

def add_book():
    """Admin function to add a new book"""
    print_header("\n=== Add New Book ===")
    
    title = Primpt.ask("Enter book title: ").strip()
    author = Primpt.ask("Enter author name: ").strip()
    isbn = Primpt.ask("Enter ISBN (optional, press Enter to skip): ").strip() or None
    
    # Get database session
    db = next(get_db())
    
    try:
        # Optional: Check if ISBN already exists
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


def admin_menu():
    """Main admin dashboard"""
    while True:
        print_header("\n=== Admin Panel ===")
        print_bold("1. Add Book")
        print_bold("2. (Future: View All Books)")
        print_bold("3. (Future: Delete Book)")
        print_bold("4. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "4":
            print_info("Returning to main menu...")
            break
        else:
            print_error("Invalid choice! Please try again.")