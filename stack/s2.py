class Stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = [str(self.list[index]) for index in range(len(self.list) - 1, -1, -1)]
        return "\n".join(values)
    
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)
        return "The element has been inserted"
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.is_empty():
            return "There is no element in the stack"
        else:
            return self.list[len(self.list) - 1]
        
    def delete(self):
        self.list = None
        
stack = Stack()

print(stack.is_empty())

stack.push(10)
stack.push(20)
stack.push(30)

print(stack)
print()

print(stack.pop())
print()

print(stack)

print(stack.peek())

