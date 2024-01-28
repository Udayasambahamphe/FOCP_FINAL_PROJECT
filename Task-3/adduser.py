import main

def add_user():
    users = main.read_passwd_file()

    # Get username and check if it's empty
    username = input("Enter new username: ")
    if not username:
        print("Error: Username is required\n")
        return

    # Check if username already exists
    if username in users:
        print("Username already exists. Try again!")
        return

    # Get real name and check if it's empty
    real_name = input("Enter real name: ")
    if not real_name:
        print("Error: Real name is required\n")
        return

    # Get password and check if it's empty
    password = input("Enter password: ")
    if not password:
        print("Error: Password is required\n")
        return

    # Encrypt the password and add the user
    encrypted_password = main.encrypt_password(password)
    users[username] = (real_name, encrypted_password)
    main.write_passwd_file(users)
    print("User Created.")

add_user()



