import string
import secrets

def generate_password(length):
    '''
    Generates a random password of the specified length.

    :param length: The length of the password to generate.
    :type length: int
    :return: A randomly generated password.
    :rtype: str
    '''
    if length < 4:
        print('password must be longer than 4 characters')
    else:
        # Concatenate all possible characters for the password
        all_strings = string.digits + string.ascii_letters + string.punctuation
        
        #Generate the password by choosing random characters from all possible characters
        password = ''.join(secrets.choice(all_strings) for i in range(length))
    
    return password


password_length = int(input('password length: '))

print(f'your password is {generate_password(password_length)}')