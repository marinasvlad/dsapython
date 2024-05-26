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

