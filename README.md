# Tabind-Scrabble (Word Combination Generator)
The objective of this project is to develop a program that takes the letter combination “tabind” and creates an alphabetical list of all the words that can be found with those letters.

This Python program generates and validates all possible word combinations from the letters "tabind" using the Collins Scrabble Words dictionary. The program finds all valid English words that can be created using these letters.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)

- ## Description
This project implements a word combination generator that:
- Generates all possible letter combinations from the input string "tabind"
- Validates each combination against the Collins Scrabble Words (2019) dictionary
- Returns an alphabetically sorted list of valid English words
- Supports combinations of varying lengths (from 2 letters up to the full length)
- Handles case-insensitive input and validation

- ## Installation
1. Clone the repository:
```bash
git clone (https://github.com/JeffreyHe9/Tabind-Scrabble.git)
```

2. Download the Collins Scrabble Words (2019) dictionary and place it in your project directory.

3. No additional Python package installation is required as the project uses only the built-in `itertools` module.

## Usage
To run the word combination generator: 
```bash
python Tabind_Scrabble.py

Output:

Found 65 valid Scrabble words using letters from 'tabind':
ab
abid
ad
adit
ai
aid
ain
ait
an
and
ani
ant
anti
at
ba
bad
bait
ban
band
bandit
bani
bant
bat
bi
bid
bin
bind
bint
bit
da
dab
daint
dan
dant
di
dib
din
dint
dit
dita
id
idant
in
it
ita
na
nab
nat
nib
nid
nit
ta
tab
tabi
tabid
tad
tai
tain
tan
ti
tian
tid
tin
tina
tind
```

## How It Works

The program consists of three main functions:

```bash 
def load_scrabble_dict(file_path):
    # Loads and processes the Scrabble dictionary
    # Returns a set of valid lowercase words

def get_all_substrings(letters):
    # Generates all possible letter combinations
    # Uses itertools.permutations for combination generation
    # Returns a set of unique combinations

def find_valid_words(letters, dictionary):
    # Validates combinations against the dictionary
    # Returns sorted list of valid words

The core functionality uses Python's `itertools.permutations` to generate all possible letter arrangements and validates them against a Scrabble dictionary.
```

## Contributing
You can contribute to this project by:

1. Adding support for custom input strings
2. Implementing performance optimizations
3. Adding unit tests
4. Improving error handling and user feedback
5. Enhancing documentation
