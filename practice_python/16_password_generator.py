# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
# uppercase letters, numbers, and symbols. The passwords should be random, generating a 
# new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random
import string


def gen_pass(length):
    partial_pass = ''
    partial_len = 0
    len_uppercase = random.randrange(1,length - 4)
    partial_len = len_uppercase
    len_symbols = random.randrange(1,length - 3 - partial_len)
    partial_len += len_symbols
    len_numbers = random.randrange(1,length - 2 -partial_len)
    partial_len += len_numbers
    len_lowercase = length - partial_len

    while len(partial_pass) <= length:
        partial_len_lowercase = 0
        partial_len_uppercase = 0
        partial_len_numbers = 0
        partial_len_symbols = 0

        type_caracter = random.randrange(1,5)
        if type_caracter == 1 and partial_len_lowercase <= len_lowercase :
            # type lowercase
            partial_pass += random.choice(string.ascii_lowercase)
            partial_len_lowercase += 1
        if type_caracter == 2 and partial_len_uppercase <= len_uppercase:
            # type uppercase
            partial_pass += random.choice(string.ascii_uppercase)
            partial_len_uppercase += 1
        if type_caracter == 3 and partial_len_numbers <= len_numbers:
            # type number
            partial_pass += random.choice(string.digits)
            partial_len_numbers += 1
        if type_caracter == 4 and partial_len_symbols <= len_symbols:
            # type symbol
            partial_pass += random.choice(string.punctuation)
            partial_len_symbols += 1

    return partial_pass


if __name__ == "__main__":
    length = int(input('Ingrese la longitud del password: '))
    password = gen_pass(length)
    print(password)