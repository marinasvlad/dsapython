class Stack:
    def __init__(self):
        self.list = [1, 2, 3, 4, 5, 6]
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

stack = Stack()
print(stack)