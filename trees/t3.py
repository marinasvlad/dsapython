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
q = Queue()