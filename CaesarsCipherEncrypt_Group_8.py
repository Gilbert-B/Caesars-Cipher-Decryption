"""
Name: Gilbert Botchway

Email: botchwaykojo@gmail.com

"""

# Decryption

# Declare Variable Characters - Upper and Lower Case
chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']

# Define Function for Plain Text and Cipher - Using a Mapping Table with maketrans() and tranlate() functions
def decode(message, offset):
    enc_chars = str.maketrans(
        f'{chars[1][offset:]}{chars[1][:offset]}{chars[0][offset:]}{chars[0][:offset]}',
        f'{chars[1]}{chars[0]}' 
    )
    return str.translate(message, enc_chars) # return a copy of the string which the characters will be mapped through the given translation table

# Set Inputs for Plain Text Message and Cipher/Shift value
get_option = input("Choose [d]ecode : ")
if get_option == 'd': 
    message = input('Enter your encoded message: ')
    offset = int(input('Choose the shift (1-26): '))
    if offset < 1 or offset > 26:
        raise Exception(f'Invalid entry: {offset}')

    else:
        print()
        print(f'Your decoded message is: {decode(message, offset)}')
