import storage
import os
import random

# Create a flashcard set in the "cards" directory
def create_set(name, text):
    curr_directory = os.getcwd()

    os.chdir("cards")

    storage.store_set(name, text)

    os.chdir(curr_directory)

# Delete a flashcard set in the "cards" directory
def process_deletion(name):
    curr_directory = os.getcwd()

    os.chdir("cards")
    
    storage.delete_set(name)

    os.chdir(curr_directory)

# Verify that the name of a set is within 30 characters and only contains alphanumeric, '-', and '_' characters
def verify_set_name(name):
    if(not len(name) > 0 or not len(name) <= 30):
        return False

    for char in name:
        if(not verify_name_char(char)):
            return False
        
    return True

# Verify whether or not a set with a given name already exists in the cards directory
def verify_name_exists(name):
    curr_directory = os.getcwd()

    os.chdir("cards")

    exists = storage.set_exists(name)

    os.chdir(curr_directory)

    return exists

# Verify that a character is alphanumeric, '-', or '_'
def verify_name_char(char):
    if(char.isalnum() or char == '-' or char == '_'):
        return True
    
    return False

# Check if changes were made to the set (in the edit set screen)
def changes_occurred(name, text):
    return text != get_set_text(name)

# Get the names of all the sets in the cards directory
def created_sets():
    curr_directory = os.getcwd()

    os.chdir("cards")

    names = storage.get_all_names()

    os.chdir(curr_directory)

    return names

# Get the text of a flashcard text file
def get_set_text(name):
    curr_directory = os.getcwd()

    os.chdir("cards")

    set_text = storage.read_set(name)

    os.chdir(curr_directory)

    return set_text

# Get the text that should be displayed on the front of a given flashcard
def show_front(card):
    return card.strip().split("~")[0]

# Get the text that should be displayed on the back of a given flashcard
def show_back(card):
    return card.strip().split("~")[1]

# Get the next card by incrementing "curr_card"; if the value is already at the max, then set it back to the minimum
def next_card(name, curr_card):
    if(curr_card < num_cards(name)):
        return curr_card + 1
    else:
        return 1
    
# Get the previous card by decrementing "curr_card"; if the value is already at the minimum, then set it back to the max
def previous_card(name, curr_card):
    if(curr_card > 1):
        return curr_card - 1
    else:
        return num_cards(name)

# Get a randomized list of each card in a given set
def get_cards(name):
    set = get_set_text(name).split("\n")
    valid_cards = []

    for card in set:
        if(is_valid_card(card)):
            valid_cards.append(card)

    random.shuffle(valid_cards)

    return valid_cards

# Determine the number of valid cards in a given set
def num_cards(name):
    set = get_set_text(name).split("\n")
    count = 0

    for card in set:
        if(is_valid_card(card)):
            count = count + 1

    return count

# Determine if a line of text is a valid representation of a flashcard
def is_valid_card(card):
    front_and_back = card.strip().split("~")

    if(len(front_and_back) >= 2):
        return True
    
    return False