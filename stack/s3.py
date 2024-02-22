class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return ' '.join(values)
        
    def is_empty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False
        
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.linked_list.head
        self.linked_list.head = new_node

custom_stack = Stack()

custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
custom_stack.push(5)

print(custom_stack)

    