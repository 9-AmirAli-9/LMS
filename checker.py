from crud import check_username

def password_check():

    flag = False

    while flag != True:
        password = input("please enter your password: ")
        if len(password) < 8 :
            print("your password is too short")

        if password.isdigit():
            print("Your password must contain letter")

    flag = True
    return password

def is_username_taken(username):
    username = username
    
    if check_username(username):
        print("this username is taken please choose another one.")
        is_username_valid()

    else:
        return username



def is_username_valid():
    flag = False
    
    while flag != True:
        username = input("enter your username: ")

        if len(username) < 5:
            print("your username is too short must contain atleast 6 character")    
            
        else:
            flag = True

    username = is_username_taken(username)
    return username


def is_phonenumber_taken():
    flag = False

    while flag != True:
        phone_number = input("enter your phone number: ")
        result=0
        # result = get_phone_number()

        if not result:
            flag = True
            return phone_number


def admin_user():
    pass