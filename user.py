from database import get_db
from crud import get_all_books, search_books, borrow_book, return_book, get_user_loans
from console import console, print_success, print_error, print_header, print_info, print_bold, Prompt


def user_menu(user):
    """user menu"""
    while True:
        console.clear()
        print_header(f"LMS - Welcome {user.username}")
        print_info(f"user: {user.username}")

        print_bold("\n1. جستجوی کتاب‌ها")
        print_bold("2. قرض گرفتن کتاب")
        print_bold("3. پس دادن کتاب")
        print_bold("4. کتاب‌های قرض گرفته شده من")
        print_bold("5. خروج از حساب")

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
        query = Prompt.ask("کلمه جستجو (عنوان، نویسنده یا ژانر)").strip()
        if not query:
            return
        books = search_books(db, query)
        if not books:
            print_error("Book not found!")
            return

        print_info(f"\nsearch result({len(books)} books):")
        for book in books:
            print_info(f"• ID: {book.id} | {book.title} | {book.author} | {book.genre}")
    finally:
        db.close()


def borrow_menu(user):
    db = next(get_db())
    try:
        list_books_simple(db)
        book_id = int(Prompt.ask("آیدی کتاب مورد نظر را وارد کنید"))

        success, message = borrow_book(db, user.id, book_id)
        if success:
            print_success(message)
        else:
            print_error(message)
    except ValueError:
        print_error("لطفا عدد وارد کنید")
    except Exception as e:
        print_error(f"خطا: {e}")
    finally:
        db.close()


def return_menu(user):
    db = next(get_db())
    try:
        loans = get_user_loans(db, user.id)
        if not loans:
            print_info("شما هیچ کتاب قرض گرفته‌ای ندارید")
            return

        console.print("\n[bold]کتاب‌های قرض گرفته شده:[/bold]")
        for loan in loans:
            console.print(f"ID قرض: {loan.id} | کتاب: {loan.book.title} | مهلت: {loan.due_date.date()}")

        loan_id = int(Prompt.ask("آیدی قرض را برای پس دادن وارد کنید"))
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
            print_info("شما هیچ کتاب قرض گرفته‌ای ندارید")
            return

        console.print("\n[bold cyan]کتاب‌های قرض گرفته شده من:[/bold cyan]")
        for loan in loans:
            status = "پس داده شده" if loan.return_date else "در حال قرض"
            console.print(f"• {loan.book.title} توسط {loan.book.author} | مهلت: {loan.due_date.date()} | وضعیت: {status}")
    finally:
        db.close()


def list_books_simple(db):
    books = get_all_books(db)
    console.print("\n[bold]لیست کتاب‌ها:[/bold]")
    for book in books:
        console.print(f"ID: {book.id} | {book.title} | {book.author}")