class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return ' '.join(values)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node


custom_queue = Queue()

custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)

print(custom_queue)
    
    
