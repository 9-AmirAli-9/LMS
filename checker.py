from crud import check_username , check_phonenumber
import re
from database import SessionLocal , get_db
from console import print_error, print_success , Prompt



def password_check():

    while True:
        password = Prompt.ask("Please enter your password: " , password=True)
        
        if len(password) < 8:
            print_error("❌ Password must be at least 8 characters long.")
            continue
        
        if not re.search(r'[A-Z]', password):
            print_error("❌ Password must contain at least one uppercase letter.")
            continue
            
        if not re.search(r'[a-z]', password):
            print_error("❌ Password must contain at least one lowercase letter.")
            continue
            
        if not re.search(r'\d', password):
            print_error("❌ Password must contain at least one digit.")
            continue
            
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print_error("❌ Password must contain at least one special character (!@#$%^&* etc).")
            continue
        
        # Optional: Ask for confirmation
        confirm = input("Confirm your password: ").strip()
        if password != confirm:
            print_error("❌ Passwords do not match. Please try again.")
            continue
            
        print_success("✅ Strong password accepted!")
        return password



def is_username_valid() -> str:
    """Validate username and check if it's taken"""
    while True:
        username = Prompt.ask("Enter your username: ")
        
        if len(username) < 5:
            print_error("❌ Username must be at least 5 characters long.")
            continue
            
        if not username.isalnum() and not '_' in username:
            print_error("❌ Username can only contain letters, numbers, and underscores.")
            continue
        
        # Check if username exists in database
        db = next(get_db())
        if check_username(db , username):          # This should return True if taken
            print_error("❌ This username is already taken. Please choose another one.")
            continue
            
        print_success("✅ Username is available!")
        return username



def is_phonenumber_valid() -> str:
    """Validate phone number format and check uniqueness"""
    while True:
        phone = Prompt.ask("Enter your phone number (e.g. 09123456789): ")
        
        # Basic Iranian phone number validation (adjust pattern for your needs)
        if not re.match(r'^09\d{9}$', phone):
            print_error("❌ Invalid phone number. Must be 11 digits starting with 09.")
            continue
        
        # Check if phone number is already registered
        db = next(get_db())
        if check_phonenumber(db , phone):          # We'll add this to crud.py
            print_error("❌ This phone number is already registered.")
            continue
            
        print_success("✅ Phone number accepted!")
        return phone


def admin_user():
    pass