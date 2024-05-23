class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        return self.list.append(value)
    
    def pop(self):
        if self.isEmpty() == False:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty() == False:
            print(self.list[len(self.list) - 1])
        else:
            print('Empty')

    def delete(self):
        self.list = None

stack = Stack()
print(stack)
print(stack.isEmpty())
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)
print(stack.isEmpty())
stack.pop()
print(stack)
stack.delete()
print(stack)