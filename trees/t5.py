from q3 import Queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
def preorder_traversal(node):
    if not node:
        return
    print(node.data, end = ' ')
    preorder_traversal(node.leftChild)
    preorder_traversal(node.rightChild)  

def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.leftChild)
    print(node.data, end = ' ')
    inorder_traversal(node.rightChild)

def postorder_traversal(node):
    if not node:
        return
    postorder_traversal(node.leftChild)
    postorder_traversal(node.rightChild)
    print(node.data, end = ' ')

def levelorder_traversal(node):
    if not node:
        return
    customQueue = Queue()
    customQueue.enqueue(node)
    while not customQueue.isEmpty():
        node = customQueue.dequeue()
        print(node.value.data)
        if node.value.leftChild is not None:
            customQueue.enqueue(node.value.leftChild)
        
        if node.value.rightChild is not None:
            customQueue.enqueue(node.value.rightChild)

def search_node(node, data):
    if not node:
        return
    
    customQueue = Queue()
    customQueue.enqueue(node)

    while not customQueue.isEmpty():
        temp = customQueue.dequeue()

        if temp.value.data == data:
            return True
        
        if temp.value.leftChild is not None:
            customQueue.enqueue(temp.value.leftChild)
        
        if temp.value.rightChild is not None:
            customQueue.enqueue(temp.value.rightChild)
    
    return False

def insert_node(node, value):
    new_node = TreeNode(value)
    if node is None:
        node = new_node
        return new_node
    
    customQueue = Queue()
    customQueue.enqueue(node)
    while not customQueue.isEmpty():
        current_node = customQueue.dequeue()

        if current_node.value.leftChild is None:
            current_node.value.leftChild = new_node
            return new_node
        
        if current_node.value.rightChild is None:
            current_node.value.rightChild = new_node
            return new_node
        
        customQueue.enqueue(current_node.value.leftChild)
        customQueue.enqueue(current_node.value.rightChild)

bt = TreeNode('Drinks')
cold = TreeNode('Cold')
hot = TreeNode('Hot')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
fanta = TreeNode('Fanta')
cola = TreeNode('Cola')
bt.leftChild = cold
bt.rightChild = hot
cold.leftChild = fanta
cold.rightChild = cola
hot.leftChild = tea
hot.rightChild = coffee
preorder_traversal(bt)
print()
inorder_traversal(bt)
print()
postorder_traversal(bt)
print()
levelorder_traversal(bt)
print()
print(search_node(bt, 'Tea'))
print()
insert_node(bt, 'Orange Juice')
levelorder_traversal(bt)

