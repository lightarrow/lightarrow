'''
palendrome finding
 I knew that I would have to loop through the input string and add all of the characters to the rear of the deck to get them into the deck.
 I chose to add each item to the rear of the deck because adding an item to the rear of the deck is a constant time operation.
 As long as the deck's size is greater than two, I would remove the front-most item and the rear-most item from the deck,
 and store each of those in their own variables. If those two variables aren't equivalent, I would return false right away.
 If the two variables are equivalent though, then I could proceed to the next pair of items.
 If the size of the deck eventually gets to be smaller than two, meaning there's only one or zero characters left in the deck,
 then I know the string is a palindrome, and I can return true. Now let's talk through how I implemented this in code.
'''


class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def check_palindrome(input_str):

    my_d = Deque()
    for char in input_str:
        my_d.add_rear(char)

    while my_d.size() >= 2:  # Size of 1 or 0 means the string is a palindrome
        front_item = my_d.remove_front()
        rear_item = my_d.remove_rear()

        if front_item != rear_item:
            return False

    return True


print(check_palindrome('racecar'))
print(check_palindrome('oranges'))