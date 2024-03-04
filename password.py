from cryptography.fernet import Fernet
import sys
import os
import sqlite3

special_characters = '~`! @#$%^&*()-_+={[]|\;:"<>,./?}'
conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()  # Create a cursor object
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    encrypted_password BLOB
                  )''')

def insert_user(name_of_service, harder_pass):
    cursor.execute('INSERT INTO users (username, encrypted_password) VALUES (?, ?)', (name_of_service, harder_pass))
    conn.commit()

def clearingline():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console 

def service_name(): #Captures the service name input from the user
    service_name = input('\033[92mPlease enter the name of the service you wish to create and save a password for: \033[0m')
    clearingline()
    return service_name

def password_input(): #Captures the password input from the user 
    pass_input = input('\033[92mPlease enter a password: \033[0m')
    clearingline()
    return pass_input

def is_valid_length(pass_input): #Function to check the length of the password is acceptable
    return len(pass_input) < 8

def has_special_characters(pass_input):
        special_char = True
        for letter in pass_input:
            if letter in special_characters:
                special_char = False
                break
        return special_char

def harder_encryption(pass_input): #Function to encrypt the password
    key = Fernet.generate_key()
    fernet = Fernet(key) 
    encMessage = fernet.encrypt(pass_input.encode())
    decMessage = fernet.decrypt(encMessage).decode()
    return encMessage

def harder_deencryption(harder_pass):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(pass_input.encode())
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage

def menu():
    chosen_path = input('''\033[92mPlease select where you would like to go next:\033[0m 
                        \033[94m1. ADD SERVICE PASSWORD\033[0m  
                        \033[94m2. SHOW ALL SAVED PASSWORDS\033[0m  
                        \033[94m3. INFO\033[0m  
                        \033[94m4. EXIT\033[0m 
: ''')
    return chosen_path
    
def exit():
    sys.exit()

def show_passwords():
    cursor.execute('SELECT * FROM users')
    for row in cursor.fetchall():
        print(row)

clearingline()

while True:
    #This section of the code requests which service the password is for and the password they wish to use.
    name_of_service = service_name()
    pass_input = password_input()
   
    
        
    if is_valid_length(pass_input):
        print('\033[92mPlease enter a password of at least 8 characters\033[0m')
    elif has_special_characters(pass_input):
        print('\033[92mPlease enter a password with at least one of the following special characters ~`! @#$%^&*()-_+={[]|\;:"<>,./?}'')\033[0m')
    else:
        print('\033[92mThank you for the acceptable password\033[0m') 
        encrypted_password = harder_encryption(pass_input)
        print(f'\033[92mYour password has now been ecrypted as: \033[0m')
        print(f'\033[95m{encrypted_password}\033[0m')

        insert_user(name_of_service, encrypted_password) #Inserts the service name and password into the database

        chosen_path = menu()

        if chosen_path == '4':
            conn.close()
            exit()
        elif chosen_path == '3':
            clearingline()
            print('''\033[94mPassword protection is important in order to protect your personal data. There is no such thing as ''Encrypted'' and ''non-Encrypted'' as there are levels to encryption that are constantly being improved upon. One major fear in the computer science community it that quantum computing is going to be able to decrypt anything with little effort or time.\033[0m''')
        elif chosen_path == '2':
            clearingline()
            show_passwords()
        elif chosen_path == '1':    
            clearingline()
            name_of_service = service_name()
    pass_input = password_input()
    clearingline()
        




    