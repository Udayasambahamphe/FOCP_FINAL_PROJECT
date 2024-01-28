import os

# Path to the password file
PASSWORD_FILE = 'passwd.txt'

def read_passwd_file():
    users = {}
    with open('passwd.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            # Check if the line is correctly formatted (username:real_name:encrypted_password)
            if len(parts) == 3:
                username, real_name, encrypted_password = parts
                users[username] = (real_name, encrypted_password)
            else:
                print(f"Warning: Ignoring malformed line: {line.strip()}")
    return users

def write_passwd_file(users):
    # Open the password file for writing
    with open(PASSWORD_FILE, 'w') as file:
        for username, (real_name, encrypted_password) in users.items():
            file.write(f"{username}:{real_name}:{encrypted_password}\n")

def encrypt_password(password):
    # Simple Caesar cipher encryption (shift by 13)
    return ''.join(chr((ord(char) - 97 + 13) % 26 + 97)     
           if char.islower()
            else char for char in password)

def decrypt_password(encrypted_password):
    # Reverse the Caesar cipher to decrypt the password
    return ''.join(chr((ord(char) - 97 - 13) % 26 + 97) 
            if char.islower() 
             else char for char in encrypted_password)

def check_user(username, password):
    users = read_passwd_file()
    if username in users:
        real_name, encrypted_password = users[username]
        # Compare the decrypted password with the input password
        return decrypt_password(encrypted_password) == password
    return False
