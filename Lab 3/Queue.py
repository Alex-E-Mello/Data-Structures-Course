#Alex Mello

#10/4/2019

#Lab 3 - SDQ

class Queue:
    """Class for the queue object"""

    def __init__(self):
        """Creates the list for the queue"""
        self.queue = []

    def enqueue(self,item):
        """Adds item to the rear of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns the item at the front of the queue"""
        item = self.queue[0]
        self.queue.remove(item)
        return item

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise"""
        length = len(self.queue)
        if length == 0:
            return True
        else:
            return False

    def size(self):
        """Returns the number of items in the queue"""
        length = len(self.queue)
        return length
