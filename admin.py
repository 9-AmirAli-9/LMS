from database import get_db   
from crud import check_isbn , create_book , delete_book , search_books , update_book
import checker as ch   
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
            if book:
                print_success("Book deleted successfully.")
        else:
            print_error("you cancel the proccess.")
            return
    except Exception as e:
        print_error(f"Error deleting book {e}")
    finally:
        db.close()

def update()
    """Admin function to update a book"""

    print_header("\n=== Update Book ===")
    id = Prompt.ask("Enter book id for update:")
    title = Prompt.ask("Enter new title: [optional]" , default = None)
    author = Prompt.ask("Enter new author: [optional]" , default = None)
    isbn = Prompt.ask("Enter new isbn: [optional]" , default = None)

        if not id or not id.isdigit():
            print_error("You must enter a valid book id!")
            return

        id = int(id)

        if not title or not author or not isbn :
            print_error("You must enter at least one field to update (title, author, or isbn)!")

        if Confirm.ask("Are you sure about this changes?"):
            db = next(get_db())

            try:
                updated_book=update_book(db=db, book_id=id, title=title, author=author, isbn=isbn )
                if updated_book:
                    print_success(f"Book with ID {book_id} updated successfully!")
                else:
                    print_error(f"Book with ID {book_id} not found!")
              
            except Exception as e:
                print_error(f"Error updating book {e}")
        else:
            print_error("The opration is canceled by user ")

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