import os
import glob

# Store a set as a text file to the "cards" directory
def store_set(name, text):
    with open(name + ".txt", "w", encoding = "utf-8") as new_file:
        new_file.write(text)

def read_set(name):
    set = open(name + ".txt", "r", encoding = "utf-8")
    text = set.read()

    set.close()

    return text

# Delete a set from the "cards" directory
def delete_set(name):
    os.remove(name + ".txt")

# Determine if a set with a given name exists in the "cards" directory
def set_exists(name):
    if(os.path.exists(name + ".txt")):

        return True

    return False

# Get the names of all sets in the "cards" directory
def get_all_names():
    return glob.glob("*.txt")