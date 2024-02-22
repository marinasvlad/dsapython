class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return(str(self.value))

class CSLinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head

        result = ''

        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1        

    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index out of range")

        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                self.tail.next = new_node

            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node

        elif index == self.length:
            self.tail.next = new_node
            new_node.next=self.head
            self.tail = new_node

        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def transverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

    def search(self, target):
        current_node = self.head
        while current_node is not None:
            if current_node.value == target:
                return True
            current_node = current_node.next
            if current_node == self.head:
                break
        return False
    
    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        
        return current_node

    def set(self, index, value):
        temp_node = self.get(index)
        if temp_node is not None:
            temp_node.value = value
            return True
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            popped_node.next = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
        
            current_node.next = self.head
            popped_node.next = None
            self.tail = current_node
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()            
        prev_node = self.get(index -1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.head = None
        self.length = 0

cs_ll  = CSLinkedList()

cs_ll.append(10)
cs_ll.append(20)
cs_ll.append(30)

print(cs_ll)

cs_ll.prepend(40)
cs_ll.prepend(50)


print(cs_ll)

cs_ll.insert(3,15)

print(cs_ll)

cs_ll.insert(1,1)

print(cs_ll)

cs_ll.insert(0,25)
print(cs_ll)

cs_ll.transverse()

print(cs_ll.search(20))

print(cs_ll.get(2))

cs_ll.set(2,85)

print(cs_ll)

cs_ll.pop_first()

print(cs_ll)
cs_ll.pop()
print(cs_ll)
cs_ll.remove(2)
print(cs_ll)

cs_ll.delete_all()
print(cs_ll)
print("End")