class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insertAtStart(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
             new_node.next = self.head
             self.head = new_node

    def __str__(self):
        str_to_return = ''
        current_node = self.head
        while current_node:
            str_to_return += str(current_node.value) + " "
            current_node = current_node.next
        return str_to_return
    

new_linked_list = LinkedList()
new_linked_list.insertAtStart(10)        
new_linked_list.insertAtStart(20)        
new_linked_list.insertAtStart(30) 
print(new_linked_list)   