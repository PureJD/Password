loop = True
while loop == True:


    def password_input():
        pass_input = input('Please enter a password: ')
        return pass_input 

    pass_input = password_input()
    print(pass_input)
    if len(pass_input) < 8: 
        print('Please enter a password at least 8')
        password_input()
    else: 
        print('Thank you for the acceptable password')



