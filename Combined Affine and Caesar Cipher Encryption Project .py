###############################################
# CSE 231 Project 4
# Algorithm
#   1. Print the banner
#   2. Get the rotation amount
#   3. Get the command
#   4. If the command is 'e', get the string to encrypt and encrypt it.
#   5. If the command is 'd', get the string to decrypt and decrypt it.
#   6. If the command is 'q', quit the program.
#   7. If the command is anything else, display an error message and get the command again.
#   8. Repeat until the command is 'q'.
###############################################
import math, string

# Define constants for punctuation and alphanumeric characters
#  string.punctuation is a string constant that contains all the punctuation characters on the keyboard.
#  except space is not included in this string
PUNCTUATION = string.punctuation

#  string.ascii_lowercase is a string constant that contains all the lowercase letters in the alphabet.
#  string.digits is a string constant that contains all the digits 0-9.
ALPHA_NUM = string.ascii_lowercase + string.digits

BANNER = ''' Welcome to the world of 'dumbcrypt,' where cryptography meets comedy! 
    We're combining Affine Cipher with Caesar Cipher to create a code 
    so 'dumb,' it's brilliant. 
    Remember, in 'dumbcrypt,' spaces are as rare as a unicorn wearing a top hat! 
    Let's dive into this cryptographic comedy adventure!             
    '''


def print_banner(message):
    '''Display the message as a banner.
    It formats the message inside a border of asterisks, creating the banner effect.'''
    border = '*' * 50
    print(border)
    print(f'* {message} *')
    print(border)
    print()


def multiplicative_inverse(A, M):
    """Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.
        Args:
        A (int): The number for which the inverse is to be found.
        M (int): The modulo value.
        Returns:
            int: The multiplicative inverse of A modulo M.
    """
    # Try all possible values
    for x in range(M):
        # Check if A * x mod M is 1
        if (A * x) % M == 1:
            return x


def check_co_prime(num, M):
    """Return True if num and M are co-prime, False otherwise.
        Args:
        num (int): The first number.
        M (int): The second number.
        Returns:
            bool: True if num and M are co-prime, False otherwise."""
    # Get gcd of num and M
    gcd_result = math.gcd(num, M)
    # Check if gcd is 1
    if gcd_result == 1:
        # Return True
        return True
    else:
        # Return False
        return False


def get_smallest_co_prime(M):
    """Return the smallest number that is co-prime with M.
        Args:
        M (int): The second number.
        Returns:
            int: The smallest number that is co-prime with M."""
    # Get smallest co-prime
    for i in range(2, M):
        if check_co_prime(i, M):
            return i


def caesar_cipher_encryption(ch, N, alphabet):
    """Return the encrypted character for ch given N and alphabet.
        Args:
        ch (str): The character to be encrypted.
        N (int): The number of rotations.
        alphabet (str): The string of characters to be used for the alphabet.
        Returns:
            str: The encrypted character."""
    # Get length of alphabet
    M = len(alphabet)
    # Get index of ch
    index = alphabet.index(ch)
    # Get new index
    new_index = (index + N) % M
    # Get new character
    new_ch = alphabet[new_index]
    # Return new character
    return new_ch


def caesar_cipher_decryption(ch, N, alphabet):
    """Return the decrypted character for ch given N and alphabet.
        Args:
        ch (str): The character to be decrypted.
        N (int): The number of rotations.
        alphabet (str): The string of characters to be used for the alphabet.
        Returns:
            str: The decrypted character."""
    # Get length of alphabet
    M = len(alphabet)
    # Get index of ch
    index = alphabet.index(ch)
    # Get new index
    new_index = (index - N) % M
    # Get new character
    new_ch = alphabet[new_index]
    # Return new character
    return new_ch


def affine_cipher_encryption(ch, N, alphabet):
    """Return the encrypted character for ch given N and alphabet.
        Args:
        ch (str): The character to be encrypted.
        N (int): The number of rotations.
        alphabet (str): The string of characters to be used for the alphabet.
        Returns:
            str: The encrypted character."""
    # Get length of alphabet
    M = len(alphabet)
    # Get smallest co-prime of M
    A = get_smallest_co_prime(M)
    # Get index of ch
    index = alphabet.index(ch)
    # Get new index
    new_index = (A * index + N) % M
    # Get new character
    new_ch = alphabet[new_index]
    # Return new character
    return new_ch


def affine_cipher_decryption(ch, N, alphabet):
    """Return the decrypted character for ch given N and alphabet.
        Args:
        ch (str): The character to be decrypted.
        N (int): The number of rotations.
        alphabet (str): The string of characters to be used for the alphabet.
        Returns:
            str: The decrypted character."""
    # Get length of alphabet
    M = len(alphabet)
    # Get index of ch
    index = alphabet.index(ch)
    # Get smallest co-prime of M
    A = multiplicative_inverse(get_smallest_co_prime(M), M)
    # Get new index
    new_index = (A * (index - N)) % M
    # Get new character
    new_ch = alphabet[new_index]
    # Return new character
    return new_ch


def main():
    """Display the banner, get the rotation amount, and get the command.
        If the command is 'e', get the string to encrypt and encrypt it.
        If the command is 'd', get the string to decrypt and decrypt it.
        If the command is 'q', quit the program.
        If the command is anything else, display an error message and get the command again.
        Repeat until the command is 'q'."""
    print_banner(BANNER)
    # Get rotation amount
    while True:
        N = input("Input a rotation (int): ")
        if N.isdigit():
            break
        else:
            print("\nError; rotation must be an integer.")
            continue
    # Get command
    while True:
        N = int(N)
        command_type = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")
        # Check command
        if command_type == 'q':
            # Quit program
            break
        elif command_type == 'e':
            # Get string to encrypt
            input_str = input("\nInput a string to encrypt: ")
            # Check for spaces
            if ' ' in input_str:
                print("\nError with character: ")
                print("Cannot encrypt this string.")
                continue
            else:
                print("\nPlain text: " + input_str)
                # Encrypt string
                e_string = ''
                # Check for punctuation
                for i in input_str:
                    if i in PUNCTUATION:
                        e_string += caesar_cipher_encryption(i, N, PUNCTUATION)
                    else:
                        i = i.lower()
                        e_string += affine_cipher_encryption(i, N, ALPHA_NUM)
                print("Cipher text: " + e_string)

        elif command_type == 'd':
            # Get string to decrypt
            d_string = input("\nInput a string to decrypt: ")
            if ' ' in d_string:
                print("\nError with character: ")
                print("Cannot decrypt this string.")
                continue
            else:
                print("\nCipher text: " + d_string)
                # Plain text
                p_str = ''
                for i in d_string:
                    # Check for punctuation
                    if i in PUNCTUATION:
                        p_str += caesar_cipher_decryption(i, N, PUNCTUATION)
                    else:
                        i = i.lower()
                        p_str += affine_cipher_decryption(i, N, ALPHA_NUM)
                print("Plain text: " + p_str)
        else:
            # Display error message
            print("\nError; command not recognized.")
            continue


if __name__ == '__main__':
    main()
