from database import get_db   # We'll make sure this exists
from crud import check_isbn , create_book
import checker as ch   # if needed later

def add_book():
    """Admin function to add a new book"""
    print("\n=== Add New Book ===")
    
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    isbn = input("Enter ISBN (optional, press Enter to skip): ").strip() or None
    
    # Get database session
    db = next(get_db())
    
    try:
        # Optional: Check if ISBN already exists
        if isbn and check_isbn(db, isbn):
            print("❌ A book with this ISBN already exists!")
            db.close()
            return
        
        book = create_book(db, title, author, isbn)
        print(f"✅ Book added successfully! ID: {book.id}")
        
    except Exception as e:
        print(f"❌ Error adding book: {e}")
    finally:
        db.close()


def admin_menu():
    """Main admin dashboard"""
    while True:
        print("\n=== Admin Panel ===")
        print("1. Add Book")
        print("2. (Future: View All Books)")
        print("3. (Future: Delete Book)")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice! Please try again.")