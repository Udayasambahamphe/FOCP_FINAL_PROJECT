import getpass  
import main  

def login():
    username = input("Username: ")
    # Securely prompting the user to enter their password (it won't be visible)
    password = getpass.getpass("Password: ")

    if main.check_user(username, password):
        print("Access granted.")  
    else:
        print("Access denied. Incorrect username or password.")  

login()  


