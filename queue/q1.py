class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end"
    
    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        else:
            return self.items.pop()
        
    def peek(self):
        if self.items == []:
            return "The queue is empty"
        else:
            return self.items[0]    
        
    def delete(self):
        self.items = None

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q)

q.dequeue()

print(q)
print(q.peek())
