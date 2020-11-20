#Alex Mello

#10/4/2019

#Lab 3 - SDQ

class Deque:
    """Class for the deque object"""

    def __init__(self):
        """Creates the list for the deque"""
        self.deque = []

    def add_front(self,item):
        """Adds item to the front of the deque"""
        self.deque.insert(0,item)

    def add_rear(self,item):
        """Adds item to the rear of the deque"""
        self.deque.append(item)

    def remove_front(self):
        """Removes and returns the item at the front of the deque"""
        item = self.deque[0]
        self.deque.remove(item)
        return item

    def remove_rear(self):
        """Removes and returns the item at the rear of the deque"""
        return self.deque.pop()

    def is_empty(self):
        """Returns True if the deque is empty, False otherwise"""
        length = len(self.deque)
        if length == 0:
            return True
        else:
            return False

    def size(self):
        """Returns the number of items in the deque"""
        length = len(self.deque)
        return length
