from database import Base , engine , SessionLocal
from models import User
import checker as ch
choice = ""


while choice != "3":
    
    print("1. Sign up")
    print("2. Sign in")
    print("3. Exit")

    choice = input("enter your choice (1/2/3): ")

    match choice :
        case "1" :
            sign_up()
        case "2":
            sign_in()
        case "3":
            pass
        case _ :
            print(" no no no")

def sign_up():
    # username password confirm_password phone_number
    username = ch.is_username_valid()
    password = ch.password_check()
    phone_number = ch.is_phonenumber_taken()
    password_confirm = input("please enter your password again: ")
    if password != password_confirm:
        print("password and confirm password does not match.")

    

def sign_in():
    pass