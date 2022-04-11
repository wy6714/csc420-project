import numpy as np
import linked_list

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
        # create a new empty table
        temp = HashMap(2 * self.number_of_buckets)
        for i in range(2 * self.number_of_buckets):
            self.table.append(None)
            entry = hash(self)

    def add(self, value):
        """
        Method to add a value to this HashMap.

        NOTE: This method should call the resize method
        if the number of items in the hash map divided by the number of buckets
        is greater than the maximum load factor.

        :param value: The string value to add to the HashMap.
        """
        # TODO:  Your code goes here.
        # Case1: added item already inside hashmap
        if self.contains(value) is True:
            return

        # Case2: if it does not need to resize:
        else:
            if (self.number_of_items / self.number_of_buckets) <= self.maximum_load_factor:
                entry = hash(value)

                #if there is no list there, make one
                if self.table[entry] is None:
                    self.table[entry] = linked_list.LinkedList()

                # add to list
                self.table[entry].add(value)

            #Case3:
            #Need to resize - (number of items / the number of buckets) > load factor
            else:


    def contains(self, value):
        """
        A method to check if the value is contained within this HashMap.
        :param value: The value to check.
        :return: boolean, True if the value is contained in the HashMap, False otherwise.
        """
        # TODO: Your code goes here.
        entry = hash(value)
        # Case1: There is no hash code for this value, return False
        if self.table[entry] is None:
            return False

        # if there is such a hash code, search needed value in this bucket
        else:
            for element in self.table[entry]:
                # Case2: Found the value in this hash code bucket, return True
                if element == value:
                    return True

                # Case3: Cannot find the value, return False
                else:
                    return False


    def to_linked_list(self):
        """
        Method to convert the HashMap to a LinkedList.
        :return: A linked list containing all items in this HashMap.
        """
        # TODO: Your code goes here.

