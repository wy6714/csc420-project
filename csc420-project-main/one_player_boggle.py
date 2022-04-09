# DO NOT MODIFY THIS FILE.

from boggle import Boggle
from hash_map import HashMap
from numpy import loadtxt
import sys

# The default name of the dictionary file.
dictionary_file_name = 'dictionary.txt'

# The default seed for randomization value.
seed_for_randomization = 100

# If the command line argument count is greater than one.
if len(sys.argv) > 1:
    # Set the seed for randomization value from the first command line argument.
    seed_for_randomization = int(sys.argv[1])

# Set the initial number of buckets in the hash map.
initial_number_of_buckets = 16

# Create and load the words array with word strings from the dictionary file.
words_array = loadtxt(dictionary_file_name, dtype='str')

# Initialize a hash map to store the dictionary words.
dictionary_hash_map = HashMap(initial_number_of_buckets)

# For each word in the words array, add it to the dictionary hash map.
for word in words_array:
    dictionary_hash_map.add(word.upper())

# Initialize our Boggle instance
boggle = Boggle(seed_for_randomization, dictionary_hash_map)

# Print the board.
boggle.print_board()

# Find all words
found_words_lists = boggle.find_all_words()

# Print the list of found words.
print(found_words_lists)

# Calculate the total points.
total_points = boggle.count_points(found_words_lists)

print(f"Total Points: {total_points}")
