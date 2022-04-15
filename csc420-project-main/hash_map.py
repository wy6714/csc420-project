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
            result += ord(character) * 31 ** (len(value) - i)
            i += 1

        return result % self.number_of_buckets

    def resize(self):
        """
        Method to resize the hash table.

        Called by the add method if the number of items in the hash map
        divided by the number of buckets is greater than the maximum load factor.
        """
        # TODO: Your code goes here.
        # Convert the hashmap to linked list
        hashmap_linkedlist = self.to_linked_list()

        # Create a new empty table with double size, and make it replace the old size table
        temp = HashMap(2 * self.number_of_buckets)
        self.table = temp

        # iterate hashmap linked list so that reinsert the items into the new size table
        list_pointer = hashmap_linkedlist.front
        while list_pointer is not None:
            self.add(list_pointer.data)
            list_pointer = list_pointer.next

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
                entry = self.hash(value)

                # if there is no list there, make one
                if self.table[entry] is None:
                    self.table[entry] = LinkedList()

                # add to list
                self.table[entry].add(value)

            # Case3:
            # Need to resize - (number of items / the number of buckets) > load factor
            else:
                self.resize()
                return self.add(value)

    def contains(self, value):
        """
        A method to check if the value is contained within this HashMap.
        :param value: The value to check.
        :return: boolean, True if the value is contained in the HashMap, False otherwise.
        """
        # TODO: Your code goes here.
        entry = self.hash(value)
        # Case1: There is no hash code for this value, return False
        if self.table[entry] is None:
            return False

        # if there is such a hash code, iterate this hash code list to search needed value
        else:
            list_pointer = self.table[entry].front
            while list_pointer is not None:
                if list_pointer.data == value:
                    return True
                list_pointer = list_pointer.next

            # Case3: Cannot find the value in the list, return false
            return False

    def to_linked_list(self):
        """
        Method to convert the HashMap to a LinkedList.
        :return: A linked list containing all items in this HashMap.
        """
        # TODO: Your code goes here.
        hashmap_linkedlist = LinkedList()
        for entry in range(self.number_of_buckets):
            if self.table[entry] is not None:
                list_pointer = self.table[entry].front
                while list_pointer is not None:
                    hashmap_linkedlist.add(list_pointer.data)
                    list_pointer = list_pointer.next
        return hashmap_linkedlist







