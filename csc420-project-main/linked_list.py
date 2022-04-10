class ListItem:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Method to initialize the LinkedList class.

        DO NOT EDIT.
        """
        # Instance variables.
        self.front = None

    def add(self, item):
        """
        Method to add a new item to the *front* of the linked list.
        :param item: The item to add to the list.
        """
        # TODO: Your code goes here.


    def contains(self, item):
        """
        Method to determine if an item is contained in the list.
        :param item: The item to check if it is contained in the list.
        :return: boolean, True if item is in the list. False otherwise.
        """

        # TODO: Your code goes here.
        # if the list is empty:
        if self.front is None:
            return False

        # if the list is not empty
        list_pointer = self.front;
        while list_pointer is not None:
            if list_pointer.data == item:
                return True
            list_pointer = list_pointer.next

        return False


    def __str__(self):
        """
        Method to return a string representation of the linked list.

        DO NOT EDIT.

        :return: A string containing the items in the linked list.
        """
        if self.front is None:
            return "empty"

        # Put all the elements (data only) into the string.
        string = ""
        list_pointer = self.front
        while list_pointer is not None:
            string += list_pointer.data + "\n"
            list_pointer = list_pointer.next

        return string
