from database import get_db
from crud import get_all_books, search_books, borrow_book, return_book, get_user_loans
from console import console, print_success, print_error, print_header, print_info, print_bold, Prompt


def user_menu(user):
    """user menu"""
    while True:
        console.clear()
        print_header(f"LMS - Welcome {user.username}")
        print_info(f"user: {user.username}")

        print_bold("\n1. Search books")
        print_bold("2. Loan book")
        print_bold("3. Return book")
        print_bold("4. My loaned book")
        print_bold("5. Log out")

        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            search_book_menu()
        elif choice == "2":
            borrow_menu(user)
        elif choice == "3":
            return_menu(user)
        elif choice == "4":
            show_my_loans(user)
        elif choice == "5":
            print_success("Goodbye!")
            break


def search_book_menu():
    db = next(get_db())
    try:
        query = Prompt.ask("search book(title , author , isbn)").strip()
        if not query:
            return
        books = search_books(db, query)
        if not books:
            print_error("Book not found!")
            return

        print_info(f"\nsearch result({len(books)} books):")
        for book in books:
            print_info(f"• ID: {book.id} | {book.title} | {book.author} | {book.isbn}")
    finally:
        db.close()


def borrow_menu(user):
    db = next(get_db())
    try:
        list_books_simple(db)
        book_id = int(Prompt.ask("Enter the ID of the desired book."))

        success, message = borrow_book(db, user.id, book_id)
        if success:
            print_success(message)
        else:
            print_error(message)
    except ValueError:
        print_error("Please enter number.")
    except Exception as e:
        print_error(f"Error: {e}")
    finally:
        db.close()


def return_menu(user):
    db = next(get_db())
    try:
        loans = get_user_loans(db, user.id)
        if not loans:
            print_info("You don't have loans")
            return

        print_bold("\n[bold]Loan books:[/bold]")
        for loan in loans:
            print_info(f"LOAN ID: {loan.id} | BOOK: {loan.book.title} | DUE DATE: {loan.due_date.date()}")

        loan_id = int(Prompt.ask("Please enter the loan id: "))
        success, message = return_book(db, user.id, loan_id)
        if success:
            print_success(message)
        else:
            print_error(message)
    finally:
        db.close()


def show_my_loans(user):
    db = next(get_db())
    try:
        loans = get_user_loans(db, user.id)
        if not loans:
            print_info("You didn't loan any books.")
            return

        print_header("\n[bold cyan]my loaned books: [/bold cyan]")
        for loan in loans:
            status = "returned" if loan.return_date else "loan"
            print_info(f"• {loan.book.title} by {loan.book.author} | due date: {loan.due_date.date()} | status: {status}")
    finally:
        db.close()


def list_books_simple(db):
    books = get_all_books(db)
    print_bold("\n[bold]Book list: [/bold]")
    for book in books:
        print_info(f"ID: {book.id} | {book.title} | {book.author}")