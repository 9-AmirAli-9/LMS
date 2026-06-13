from crud import check_username , check_phonenumber
import re
from database import SessionLocal , get_db
def password_check():

    while True:
        password = input("Please enter your password: ").strip()
        
        if len(password) < 8:
            print("❌ Password must be at least 8 characters long.")
            continue
        
        if not re.search(r'[A-Z]', password):
            print("❌ Password must contain at least one uppercase letter.")
            continue
            
        if not re.search(r'[a-z]', password):
            print("❌ Password must contain at least one lowercase letter.")
            continue
            
        if not re.search(r'\d', password):
            print("❌ Password must contain at least one digit.")
            continue
            
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("❌ Password must contain at least one special character (!@#$%^&* etc).")
            continue
        
        # Optional: Ask for confirmation
        confirm = input("Confirm your password: ").strip()
        if password != confirm:
            print("❌ Passwords do not match. Please try again.")
            continue
            
        print("✅ Strong password accepted!")
        return password



def is_username_valid() -> str:
    """Validate username and check if it's taken"""
    while True:
        username = input("Enter your username: ").strip()
        
        if len(username) < 5:
            print("❌ Username must be at least 5 characters long.")
            continue
            
        if not username.isalnum() and not '_' in username:
            print("❌ Username can only contain letters, numbers, and underscores.")
            continue
        
        # Check if username exists in database
        db = next(get_db())
        if check_username(db , username):          # This should return True if taken
            print("❌ This username is already taken. Please choose another one.")
            continue
            
        print("✅ Username is available!")
        return username



def is_phonenumber_valid() -> str:
    """Validate phone number format and check uniqueness"""
    while True:
        phone = input("Enter your phone number (e.g. 09123456789): ").strip()
        
        # Basic Iranian phone number validation (adjust pattern for your needs)
        if not re.match(r'^09\d{9}$', phone):
            print("❌ Invalid phone number. Must be 11 digits starting with 09.")
            continue
        
        # Check if phone number is already registered
        db = next(get_db())
        if check_phonenumber(db , phone):          # We'll add this to crud.py
            print("❌ This phone number is already registered.")
            continue
            
        print("✅ Phone number accepted!")
        return phone


def admin_user():
    pass