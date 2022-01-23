'''FIFO Queues
#right = end of a list
# remove items from the queue in constant time
# runtime is O(1), or constant time
# remove from the left O(n) linear time.
enqueue()
dequeue()
peek()
size()
empty()
Recursion  Queues are recursive
'''


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # insert an item into zeroth element of the list.
        """
        runtime is O(n), or linear time because inserting into 0th indexk forcers all other items to move one index to the left.
        :param item:
        :return:
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Returnd and removes the front-most item of the Queue, which id represented by the last item in the list.
        The runtime is O(1) or constant time because indexing to the end of a list happens in constant time.
        :return:
        """
        if self.items:
            return self.items.pop()

    def peek(self):
        """
        :returns the last item in the list. that represents the front-most item in the queue
        Runtime O(1) constant time indexing to the last item and returning the value.
        :return:
        """
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        """

        :return: The size of the queue that is the length of the queue.
        runtime O(1) constant time, because we areturn only the lengeth.

        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean weather the queue is empty.
        O(1) or constant as checking for equality.
        :return:
        """
        return self.items == []
