#The objective of this project is to develop a program that takes the letter combination “tabind”
#and creates an alphabetical list of all the words that can be found with those letters.

#Imports the permutations function which generates all possible arrangements of items in different orders.
from itertools import permutations

#Defines function with default file path
def load_scrabble_dict(file_path=r'D:\EMRTS_Code\.venv1\Collins Scrabble Words (2019).txt'):
#Opens file in read mode ('r'). Remove whitespace (strip()). Convert to lowercase (lower()). Create set of unique words
    try:
        with open(file_path, 'r') as file:
            return {word.strip().lower() for word in file}
    #Handles missing file error. Returns empty set if file not found
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Download SOWPODS dictionary first.")
        return set()

# generates all possible word combinations from given letters
def get_all_substrings(letters):
    #Converts input to lowercase
    letters = letters.lower()
    substrings = []
    #Generates lengths from 2 to max letters
    for length in range(2, len(letters) + 1):
        #Creates all possible arrangements of specified length
        for combo in permutations(letters, length):
            # Combines letter tuples into strings
            substrings.append(''.join(combo))
    #Returns unique combinations
    return set(substrings)

#Brings everything together and run the project
def find_valid_words(letters, dictionary):
    #Gets all possible letter combinations
    possible_words = get_all_substrings(letters)
    #Creates set of words that exist in Scrabble dictionary
    valid_words = {word for word in possible_words if word in dictionary}
    #Returns alphabetically sorted valid words
    return sorted(valid_words)

def main():
    letters = "tabind"
    scrabble_dict = load_scrabble_dict()

    if not scrabble_dict:
        return

    valid_words = find_valid_words(letters, scrabble_dict)

    print(f"\nFound {len(valid_words)} valid Scrabble words using letters from '{letters}':")
    for word in valid_words:
        print(word)

if __name__ == "__main__":
    main()