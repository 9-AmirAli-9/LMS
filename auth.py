from database import SessionLocal
import checker as ch
from crud import check_username, check_phonenumber, create_user, authenticate_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def sign_up():
    """Complete secure sign up"""
    print("\n=== Sign Up ===")
    
    db = next(get_db())
    try:
        # Use checker functions
        username = ch.is_username_valid()           # Now uses crud check
        password = ch.password_check()
        phonenumber = ch.is_phonenumber_valid()
        
        is_admin = ch.admin_user()
        
        # Create user using CRUD
        create_user(db, username, password, phonenumber, is_admin)
        
        print(f"\n✅ Account successfully created for '{username}'!")
        
    except Exception as e:
        print(f"❌ Registration failed: {e}")
    finally:
        db.close()


def sign_in():
    """Sign in using CRUD authentication"""
    print("\n=== Sign In ===")
    
    db = next(get_db())
    try:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        
        user = authenticate_user(db, username, password)
        
        if user:
            print(f"\n✅ Welcome back, {username}!")
            if user.is_admin:
                print("👑 Admin privileges activated.")
            # TODO: Later redirect to main menu
        else:
            print("❌ Invalid username or password.")
            
    except Exception as e:
        print(f"❌ Sign in error: {e}")
    finally:
        db.close()


# Main menu
def main_auth():
    while True:
        print("\n" + "="*40)
        print("          LMS - Authentication")
        print("="*40)
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main_auth()