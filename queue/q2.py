class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
            self.LinkedList.tail = new_node
        else:
            self.LinkedList.tail.next = new_node
            self.LinkedList.tail = new_node
        
        return new_node
    
    