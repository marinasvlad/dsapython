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
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False
    
    def dequeue(self):
        if not self.isEmpty():
            removed = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            
            return removed
    
    def peek(self):
        if not self.isEmpty():
            return self.LinkedList.head.value
        
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print()
print(q)
q.dequeue()
print(q.peek())
print()
print(q)