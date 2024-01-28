import main

def delete_user():
    users = main.read_passwd_file()

    username = input("Enter username: ")
    if username not in users:
        print("User not found.")
        return

    del users[username]
    main.write_passwd_file(users)
    print("User Deleted .")

delete_user()

