import numpy as np
from linked_list import LinkedList


class HashMap:
    def __init__(self, number_of_buckets):
        """
        Method to initialize the HashMap class.

        DO NOT EDIT.
        """
        # The maximum load factor
        self.maximum_load_factor = 0.75

        # Initial number of buckets.
        self.number_of_buckets = number_of_buckets

        # The hashtable.
        self.table = np.empty(self.number_of_buckets, dtype='object')

        # Keep track of number of items added.
        self.number_of_items = 0

    def hash(self, value):
        """
        The hash code method to find the index into the table given a string value.

        DO NOT EDIT.

        :param value: A string value.
        :return: The hash code index into the hash table.
        """
        result = 0
        i = 1
        for character in value:
            result += ord(character) * 31**(len(value) - i)
            i += 1

        return result % self.number_of_buckets

    def resize(self):
        """
        Method to resize the hash table.

        Called by the add method if the number of items in the hash map
        divided by the number of buckets is greater than the maximum load factor.
        """
        # TODO: Your code goes here.


    def add(self, value):
        """
        Method to add a value to this HashMap.

        NOTE: This method should call the resize method
        if the number of items in the hash map divided by the number of buckets
        is greater than the maximum load factor.

        :param value: The string value to add to the HashMap.
        """
        # TODO:  Your code goes here.


    def contains(self, value):
        """
        A method to check if the value is contained within this HashMap.
        :param value: The value to check.
        :return: boolean, True if the value is contained in the HashMap, False otherwise.
        """
        # TODO: Your code goes here.


    def to_linked_list(self):
        """
        Method to convert the HashMap to a LinkedList.
        :return: A linked list containing all items in this HashMap.
        """
        # TODO: Your code goes here.

