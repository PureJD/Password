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
        special_char = False
        for letter in pass_input:
            if letter in special_characters:
                special_char == True 
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

        
    if is_valid_length(pass_input):
        print('Please enter a password of at least 8 characters')
    elif has_special_characters(pass_input):
        
        print('Please enter a password with at least one of the following special characters ~`! @#$%^&*()-_+={[]|\;:"<>,./?}'')')
    else:
        print('Thank you for the acceptable password') 
        encrypt_password = encrypt(pass_input)
        print(f'Your password has now been ecrypted as {encrypt_password}')

    


    