from database import SessionLocal
import checker as ch
from crud import check_username, check_phonenumber, create_user, authenticate_user
from admin import admin_menu
from console import console, print_success, print_error, print_header , Prompt , print_bold
from user import user_menu


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ثبت نام
def sign_up():
    """Complete secure sign up"""
    print_header("\n=== Sign Up ===")
    
    db = next(get_db())
    try:
        
        username = ch.is_username_valid()           
        password = ch.password_check()
        phonenumber = ch.is_phonenumber_valid()
        
        create_user(db, username, password, phonenumber)
        
        print_success(f"\n Account successfully created for '{username}'!")
        
    except Exception as e:
        print_error(f" Registration failed: {e}")
    finally:
        db.close()

#  ورود
def sign_in():
    """Sign in using CRUD authentication"""
    print_header("\n=== Sign In ===")
    
    db = next(get_db())
    try:
        username = Prompt.ask("Enter your username: ").strip()
        
        password = Prompt.ask("Enter your password: " , password=True).strip()
        
        user = authenticate_user(db, username, password)
        
        if user:
            print_success(f"\n Welcome back, {username}!")
            if user.is_admin:
                print_success("Admin privileges activated.")
                admin_menu()
            else:
                user_menu(user)
            return
            
        else:
            print_error("Invalid username or password.")
            
    except Exception as e:
        print_error(f"Sign in error: {e}")
    finally:
        db.close()


# Main menu
def main_auth():
    while True:
        console.clear() 

        print_header("LMS - Library Management System")
        print_bold("\n1. Sign Up")
        print_bold("2. Sign In")
        print_bold("3. Exit")
        
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3"])
        
        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            print_success("Goodbye!")
            break


if __name__ == "__main__":
    main_auth()