#done
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return self.data

class LinkedList:
    #works
    def __init__(self):
        self.head = None

    #works
    def add(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp    

    #works
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next
        return count

    #should work
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self,item):
        current = self.head
        previous = None
        while current != None:
            if current.data == item:
                if previous == None:
                    self.head = current.next
                    return
                if previous != None and current.next == None:
                    previous.next = None
                    return
                if previous != None and current.next != None:
                    previous.next = current.next
                    return         
            else:
                previous = current
                current = current.next

    #should work
    def append(self,item):
        current = self.head
        temp = Node(item)
        if current == None:
            self.head = temp
        else:
            while current != None and current.next != None:
                current = current.next
            current.next = temp
            
    def pop(self, pos = None):
        current = self.head
        previous = None
        counter = 0
        if pos == None:
            while current != None:
                if current.next == None and previous != None:
                    previous.next = None
                    return current.data
                if current.next == None and previous == None:
                    self.head = None
                    return current.data
                if current.next != None:
                    previous = current
                    current = current.next
        if pos == 0:
            if current != None:
                if current.next != None:
                    self.head = current.next
                    return current.data
                
        else:
            while current != None:
                if counter == pos:
                    if current.next == None:
                        previous.next = None
                        return current.data
                    elif previous != None:
                        temp = current.data
                        current = current.next
                        previous.next = current
                        return temp
                else:
                    previous = current
                    current = current.next
                    counter = counter + 1

    #should work
    def search(self,item):
        current = self.head
        found = False
        last = False
        while not found and not last and current != None:
            if current.data == item:
                return True
            if current.next == None and current.data != item:
                return False
            else:
                current = current.next

    #should work
    def remove(self,item):
        current = self.head
        previous = None
        while current != None:
            if current.data == item:
                if current.next == None:
                    previous.next = None
                    return current.data
                if current.next != None and previous != None:
                    current = current.next
                    previous.next = current
                    return
                if current.next != None and previous == None:
                    self.head = current.next
                    return
            else:
                previous = current
                current = current.next
                
    #works
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
            
    #works
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False











