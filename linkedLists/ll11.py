class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:    
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        if self.head is None:
            print('Empty')
        else:
            temp_node = self.head
            for _ in range(self.length):
                print(temp_node.value, end = ' ')
                temp_node = temp_node.next

    def search(self, value):
        temp_node = self.head
        index = 0 
        while temp_node is not None:
            if temp_node.value == value:
                return "Found at index " + str(index)
            temp_node = temp_node.next
            index += 1
        return "Not found"
    
    def get(self, index):
        if index >= self.length or index < 0:
            print("Index out of range")
            return None
        else:
            if index == 0:
                return self.head
            else:
                temp_node = self.head
                current_index = 0
                while current_index < index:
                    temp_node = temp_node.next
                    current_index += 1
                return temp_node
        
    def set(self, index, value):
        if index >= self.length or index < 0:
            return -1
        else:
            temp = self.get(index)
            temp.value = value
    
    def pop_first(self):
        if self.head is None:
            return False
        else:
            if self.length == 1:
                self.head = None
                self.tail = None
                self.length = 0
            else:
                self.head = self.head.next
            self.length -= 1
            return True

                
new_linked_list = LinkedList()

new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
print(new_linked_list)
new_linked_list.prepend(50)
print(new_linked_list)
new_linked_list.insert(0,60)
print(new_linked_list)
new_linked_list.traverse()
print()
print(new_linked_list.search(50))
print()
new_linked_list.set(3,25)
print(new_linked_list)
new_linked_list.pop_first()
print(new_linked_list)
