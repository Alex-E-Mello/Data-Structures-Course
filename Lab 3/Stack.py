#Alex Mello

#10/4/2019

#Lab 3 - SDQ

class Stack:
    """Class for the stack object"""
    
    def __init__(self):
        """Creates the list for the stack"""
        self.stack = []

    
    def push(self,item):
        """Adds item to the top of the stack"""
        self.stack.append(item)

    def pop(self):
        """Removes and returns the top item in the stack"""
        return self.stack.pop()

    def peek(self):
        """Returns the top item on the stack, but does not remove it"""
        index = len(self.stack)-1
        return self.stack[index]

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise"""
        length = len(self.stack)
        if length == 0:
            return True
        else:
            return False

    def size(self):
        """Returns the number of items on the stack"""
        length = len(self.stack)
        return length
