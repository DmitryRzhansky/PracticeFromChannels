import pyAesCrypt
import os

# File decryption function

def decryption(file, password):

    # Set the buffer size
    buffer_size = 512 * 1024

    # Calling the decryption method

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # Displaying the name of the encrypted file

    print("[File '" + str(os.path.splitext(file)[0]) + "' encrypted]")

    # Deleting the source file

    os.remove(file)

# Directory scanning function

def walking_by_dirs(dir, password):

    # Loop through all subdirectories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # If we find a file, we decrypt it
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                 print(ex)
        # If we find a directory, we repeat the cycle looking for files
        else:
            walking_by_dirs(path, password)

password = input("Enter your password for decryption: ")
walking_by_dirs("", password)