import hashlib
import getpass

# Name of the password file and the encrypted file
filename = "passwords.txt"
encrypted_filename = "encrypted_passwords.txt"

# Take the keyword and extra password for the password file
keyword = getpass.getpass(prompt="Please enter the keyword for the password file: ")
extra_password = getpass.getpass(prompt="Please enter your extra password:  ")
# The encryption algorithm to be used
algorithm = "sha256"

# The function to encrypt the password file
def encrypt_password_file(filename, keyword, extra_password, algorithm, encrypted_filename):
    with open(filename, 'r') as f:
        data = f.read()
        # Encrypt the data using the keyword and extra password
        encrypted_data = hashlib.new(algorithm, keyword.encode() + extra_password.encode() + data.encode()).hexdigest()
        # Write the encrypted data to a new file
        with open(encrypted_filename, 'w') as fw:
            fw.write(encrypted_data)

# Example usage: Encrypt the password file
encrypt_password_file(filename, keyword, extra_password, algorithm, encrypted_filename)
