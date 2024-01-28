import getpass
import main

def change_password():
     # Checking if the entered username exists in the users dictionary
    users = main.read_passwd_file()

    username = input("Username: ")
    if username not in users:
        print("User not found.")
        return

    current_password = getpass.getpass("Current Password: ")
    if not main.check_user(username, current_password):
        print("Failed password.")
        return

    new_password = getpass.getpass("Enter New Password: ")
    confirm_password = getpass.getpass("Confirm your password: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return
    
    # Updating the user's password in the users dictionary
    users[username] = (users[username][0], main.encrypt_password(new_password))
    # Writing the updated users data back to the password file
    main.write_passwd_file(users)
    print("Password changed .")

change_password()

