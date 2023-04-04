import os

# Create a directory for each letter of the alphabet
for letter in range(ord("A"), ord("Z") + 1):
    dir_name = chr(letter)
    os.mkdir(dir_name)
    print(f"A directory called '{dir_name}' has been created.")
