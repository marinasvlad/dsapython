class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    
    def enqueue(self, value):
        self.items.append(value)
    
    def dequeue(self):
        if not self.isEmpty():
            self.items.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
    
    def delete(self):
        self.items = None
