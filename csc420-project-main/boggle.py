from hash_map import HashMap
import numpy as np

# The number of dice on the boggle board.
BOGGLE_NUM_DICE = 25

# The number of sides on each individual dice.
BOGGLE_DICE_SIDES = 6

# The dimensions of the boggle board.
BOGGLE_DIMENSION = 5

# The twenty-five possible boggle dice, each with six lettered sides.
BOGGLE_DICE = [
    "AAAFRS", "AAEEEE", "AAFIRS", "ADENNN", "AEEEEM",
    "AEEGMU", "AEGMNN", "AFIRSY", "BJKQXZ", "CCENST",
    "CEIILT", "CEILPT", "CEIPST", "DDHNOT", "DHHLOR",
    "DHLNOR", "DHLNOR", "EIIITT", "EMOTTT", "ENSSSU",
    "FIPRSY", "GORRVW", "IPRRRY", "NOOTUW", "OOOTTU",
]

# The word scores. (key = word length, value = points)
BOGGLE_WORD_SCORES = {3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11, 9: 11}


class Boggle:
    def __init__(self, seed_for_randomization, dictionary_hash_map):
        """
        Method to initialize the Boggle class.

        DO NOT EDIT.
        """

        # Store the dictionary for later use.
        self.dictionary_hash_map = dictionary_hash_map

        # Initialize an empty boggle board as a two dimensional array of size boggle dimension.
        self.boggle_board = np.empty((BOGGLE_DIMENSION, BOGGLE_DIMENSION), dtype='object')

        # Setup a random number generator using the seed passed into the init method.
        random_number_generator = np.random.default_rng(seed_for_randomization)

        # Setup the board by rolling dice
        dice_used_on_board = np.zeros(BOGGLE_NUM_DICE)
        for row in range(BOGGLE_DIMENSION):
            for column in range(BOGGLE_DIMENSION):
                while True:
                    # Randomly choose a dice to roll.
                    dice_to_roll = random_number_generator.integers(low=0, high=BOGGLE_NUM_DICE)
                    if dice_used_on_board[dice_to_roll] == 1:
                        # Keep choosing a dice if this one has already been rolled.
                        continue

                    # Randomly choose a side of the dice.
                    side_of_dice = random_number_generator.integers(low=0, high=BOGGLE_DICE_SIDES)
                    self.boggle_board[row][column] = BOGGLE_DICE[dice_to_roll][side_of_dice]
                    # Mark that dice as rolled
                    dice_used_on_board[dice_to_roll] = 1
                    break

    def print_board(self):
        """
        Method to print the Boggle board.

        DO NOT EDIT.
        """

        print(".-----------.")
        for row in range(BOGGLE_DIMENSION):
            print("| ", end='')
            for column in range(BOGGLE_DIMENSION):
                print(self.boggle_board[row][column], end='')
                if self.boggle_board[row][column] == 'Q':
                    print("u", end='')
                else:
                    print(" ", end='')

            print("|")

        print("'-----------'")

    def count_points(self, found_words):
        """
            Method to count the points up.
            3 and 4 length words are worth 1 point
            5 length worth 2
            6 length worth 3
            7 length worth 5
            8 length worth 11
            note we stop searching at 8 length words.

            DO NOT EDIT.

            :param found_words: a linked list of found words
            :return: the Boggle total score resulting from the list of words
        """

        # Initialize a total score variable to track the score.
        total_score = 0

        # Start at the front of the found words linked list.
        list_pointer = found_words.front
        while list_pointer is not None:
            # If the word is in the dictionary.
            if self.dictionary_hash_map.contains(list_pointer.data):
                # Add the word score to the total score.
                total_score += BOGGLE_WORD_SCORES.get(len(list_pointer.data), 0)
            # Advance the list pointer.
            list_pointer = list_pointer.next
        return total_score

    def find_all_words(self):
        """
        Entry method for finding all the words.

        DO NOT EDIT.

        :return: A linked list of all found words on the Boggle board.
        """

        # A zeroed out 2 dimensional array.
        # Currently visited there are no visited squares on the Boggle board.
        visited = np.zeros((BOGGLE_DIMENSION, BOGGLE_DIMENSION))

        # The current word is empty.
        current_word = ""

        # Set the initial number of buckets in the hash map.
        initial_number_of_buckets = 16

        # Initialize a hashmap to track the words that have been found so far.
        found_words_hash_map = HashMap(initial_number_of_buckets)

        # Start a recursion at every square on the Boggle board.
        for row in range(BOGGLE_DIMENSION):
            for column in range(BOGGLE_DIMENSION):
                self.boggle_all_words(found_words_hash_map, row, column, current_word, visited)

        # Return a linked list of found words.
        return found_words_hash_map.to_linked_list()

    def boggle_all_words(self, found_words_hash_map, row, column, current_word, last_visited):
        """
        Recursive function to find all words. Starting at a specific row, column.

        :param found_words_hash_map: A hash map containing the words found so far.
        :param row: The current row on to Boggle board.
        :param column: The current column on to Boggle board.
        :param current_word: The current word constructed by moving over the Boggle board.
        :param last_visited: The last visited 2-dimensional numpy array.
                             To track which dice on to Boggle board have been visited.
        :return:
        """

        #
        # Basic Algorithm:
        # 1. Return out of recursion if ...
        #    - the word is too long (only words up to 8)
        #    - the row/column is off the board
        #    - already visited this dice
        # 2. Consider the current word which is the last word with letter at row/column appended to it
        #    - current_word = current_word + self.boggle_board[row][column]
        #    - be careful about Q's (they get a free U)!
        # 3. Is the current word a word greater than length 2?
        #    - self.dictionary_hash_map.contains(current_word)
        #    and have I not found it yet?
        #    - found_words_hash_map.contains(current_word)
        #    If so, save it in the found words hashmap
        # 4. Mark this row/column as visited
        # 5. Perform 8 recursion for all possible next row/column
        #    - note that the first thing you do in this function is check
        #      if the recursion should return so there's no need to check,
        #      just do the recursive call!
        #
        # Some gotchas!
        #  - Be careful about pointers/arrays -- where exactly is the memory accessing?
        #  - Be careful about strings and appending -- be sure to null terminate!
        #  - Memory errors compound -- check valgrind often!
        #
        # Some tips!
        #  - try setting your max word length to 3 for testing
        #  - try printing the current word and the visited to track your algorithm path
        #    * (BUT DON'T SUBMIT CODE WITH EXTRA PRINTS)
        #

        # Make a deep copy of the last_visited array because numpy arrays are passed by reference.
        visited = np.ndarray.copy(last_visited)

        # TODO: Your code goes here.
        # 1. return out of recursion
        # 1.1 if the length of current word up to 8
        if len(current_word) >= 8:
            return

        """
        four conner and four inside separately recursion
        # if on edge column of board
        # (0,0) -> only go right/down right/down
        if row == 0 and column == 0:
            self.boggle_all_words(found_words_hash_map, row, column + 1, current_word, visited)      # RIGHT
            self.boggle_all_words(found_words_hash_map, row + 1, column + 1, current_word, visited)  # DOWN RIGHT
            self.boggle_all_words(found_words_hash_map, row + 1, column, current_word, visited)      # DOWN

        # (0,5) -> only go left/down left/down
        elif: row == 5 and column == 0:
            self.boggle_all_words(found_words_hash_map, row, column - 1, current_word, visited)      #LEFT
            self.boggle_all_words(found_words_hash_map, row + 1, column - 1, current_word, visited)  # DOWN LEFT
        """

        # 1.2 if the row/column is off board
        if row < 0 or row > 4 or column < 0 or column > 4:
            return

        # 1.3 already visited this dice
        if visited[row][column] == 1:
            return

        # 2. if current word which is the last word with letter at row/column appended to it
        # if the last letter is Q, get free U
        if self.boggle_board[row][column] == 'Q':
            current_word = current_word + 'QU'
        else:
            current_word = current_word + self.boggle_board[row][column]

        # 3. if len(current_word)>2
        #       and if the current word is inside the dictionary,
        #       and if this word has not been found yet,
        # add to found_word_hash_map
        if len(current_word) > 2 \
                and self.dictionary_hash_map.contains(current_word) is True \
                and found_words_hash_map.contains(current_word) is False:

            found_words_hash_map.add(current_word)

            print(current_word)

        # mark this row/column as visited
        visited[row][column] = 1

        # Perform 8 recursive calls on all surrounding Boggle dice.
        # Note that we check base case conditions at the start of the recursive call.
        # So we just need to make the recursive calls to the surrounding Boggle letters.
        # You get this for free.
        self.boggle_all_words(found_words_hash_map, row - 1, column, current_word, visited)  # UP
        self.boggle_all_words(found_words_hash_map, row - 1, column - 1, current_word, visited)  # UP LEFT
        self.boggle_all_words(found_words_hash_map, row - 1, column + 1, current_word, visited)  # UP RIGHT
        self.boggle_all_words(found_words_hash_map, row + 1, column, current_word, visited)  # DOWN
        self.boggle_all_words(found_words_hash_map, row + 1, column - 1, current_word, visited)  # DOWN LEFT
        self.boggle_all_words(found_words_hash_map, row + 1, column + 1, current_word, visited)  # DOWN RIGHT
        self.boggle_all_words(found_words_hash_map, row, column - 1, current_word, visited)  # LEFT
        self.boggle_all_words(found_words_hash_map, row, column + 1, current_word, visited)  # RIGHT
