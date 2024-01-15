import sys
while True:
    
    #Captures the password input from the user 
    def password_input():
        pass_input = input('Please enter a password: ')
        return pass_input
    
    #Variable to hold the password input
    pass_input = password_input()
    special_characters = '~`! @#$%^&*()-_+={[]|\;:"<>,./?}'

    #Function to check the length of the password is acceptable
    def is_valid_length(pass_input):
        return len(pass_input) < 8
    
    def has_special_characters(pass_input):
        special_char = True
        for letter in pass_input:
            if letter in special_characters:
                special_char = False
                break
        return special_char
            
    #Encrypts the password with a very simple encryption. Considerations can be used to convert arrays into a dictionary also. This method allows further encryption by adding further values to indexing.  
    def encrypt(password):
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`! @#$%^&*()-_+={[]|\;:"<>,./?}'
        cryptobet = 'tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`! @#$%^&*()-_+={[]|\;:"<>,./?}abcdefghijklmnopqr'
        encrypt_password = ''
        for letter in password:
            index = alphabet.index(letter) 
            encrypt_password += cryptobet[index]
        return encrypt_password

    def menu():
        chosen_path = input('Please select where you would like to go next: 1. ANOTHER PASSWORD  2. HARDER ENCRYPTION  3. INFO  4. EXIT  :')
        return chosen_path
    
    def exit():
        sys.exit()

        
    if is_valid_length(pass_input):
        print('Please enter a password of at least 8 characters')
    elif has_special_characters(pass_input):
        print('Please enter a password with at least one of the following special characters ~`! @#$%^&*()-_+={[]|\;:"<>,./?}'')')
    else:
        print('Thank you for the acceptable password') 
        encrypted_password = encrypt(pass_input)
        print('Your password has now been ecrypted as ' + encrypted_password)
        chosen_path = menu()
        if chosen_path == '4':
            exit()
        elif chosen_path == '3':
            print('Password protection is important in order to protect your personal data. There is no such thing as ''Encrypted'' and ''non-Encrypted'' as there are levels to encryption that are constantly being improved upon. One major fear in the computer science community it that quantum computing is going to be able to decrypt anything with little effort or time.')
    



    