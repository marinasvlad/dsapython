class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        return '\n'.join([str(x.value) for x in self.LinkedList])

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.LinkedList.head
        self.LinkedList.head = new_node
        return new_node

    def pop(self):
        if not self.isEmpty():
            self.LinkedList.head = self.LinkedList.head.next
            return self.LinkedList.head
        return None
    
    def peek(self):
        if not self.isEmpty():
            print(self.LinkedList.head.value)
    
    def delete(self):
        self.LinkedList.head = None

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print(stack)
stack.pop()
print()
print(stack)
print()
stack.peek()