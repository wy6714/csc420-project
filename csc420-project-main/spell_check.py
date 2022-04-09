# DO NOT MODIFY THIS FILE.

from hash_map import HashMap
from numpy import loadtxt
import sys

# The default name of the dictionary file.
dictionary_file_name = 'dictionary.txt'

# If the command line argument count is greater than one.
if len(sys.argv) > 1:
    # Set the dictionary file name from the first command line argument.
    dictionary_file_name = sys.argv[1]

# Set the initial number of buckets in the hash map.
initial_number_of_buckets = 16

# Create and load the words array with word strings from the dictionary file.
words_array = loadtxt(dictionary_file_name, dtype='str')

# Initialize a hash map to store the dictionary words.
dictionary_hash_map = HashMap(initial_number_of_buckets)

# For each word in the words array, add it to the dictionary hash map.
for word in words_array:
    dictionary_hash_map.add(word)


# Continuously prompt the user for a word.
while True:
    # Try to ead user input.
    try:
        # Create a spellcheck prompt.
        user_input = input("spellcheck> ")
    # Catch an EOF, end of file signal, i.e. Control-D.
    except EOFError:
        # If an EOF was caught, then break out of the while loop.
        print()
        break

    # Split the input into space separated words.
    # For each word check to see if it is in the dictionary.
    for word in user_input.split():
        if dictionary_hash_map.contains(word.lower()):
            print(f"{word} -> word")
        else:
            print(f"{word} -> not a word")
