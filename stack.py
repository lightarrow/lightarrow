#!/bin/env python3
#Create a stack to use as a datatype for challenges.

class Stack:
    """
    :optimization:
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        accepts and item as a parameter adn appends it to the end of the list.
        :runtime: is O(1), or constant time, because appending to the end of a list happens in constant time.
        :param item:
        :return:
        """

        self.items.append(item)

    def pop(self):
        """
        Removes and returns the last item for the list with is also the item of the Stack
        :optimizaion: O(1)
        The runtime is constant time, because all it does is index to the last item of the list.
        :return:
        """
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        """
        Shows the item at the top of the stack(last position)
        :Runtime:
        O(1) The runtime is constant time, because all it does is index into a list.
        :return:
        :optimization:
        """
        return self.items[-1]

    def size(self):
        """
        :runtime:
        O(1) The runtime is constant time, because finding the length of a list is in constant time.
        :return:
        """
        return len(self.items)

    def is_empty(self):
        """
        :runtime:
        O(1) The runtime is constant time, as testing for equality is in constant time.
        :return: type: boolean true if list is empty
        """
        return self.items == []