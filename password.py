while True:
    #Captures the password input from the user 
    def password_input():
        pass_input = input('Please enter a password: ')
        return pass_input
    
    #Variable to hold the password input
    pass_input = password_input()

    #Function to check the length of the password is acceptable
    def is_valid_length(pass_input):
        return len(pass_input) < 8

    #Encrypts the password with a very simple encryption. Considerations can be used to convert arrays into a dictionary also. This method allows further encryption by adding further values to indexing.  
    def encrypt(password):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0','1','2','3','4','5','6','7','8','9']
        cryptobet = ['t', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0','1','2','3','4','5','6','7','8','9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
        encrypt_password = ''
        for letter in password:
            index = alphabet.index(letter) 
            encrypt_password += cryptobet[index]
        return encrypt_password

        
    if is_valid_length(pass_input):
        print('Please enter a password of at least 8 characters')
    else:
        print('Thank you for the acceptable password') 
        encrypt_password = encrypt(pass_input)
        print(f'Your password has now been ecrypted as {encrypt_password}')

    


    