class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root, node_value):
    if root.data == None:
        root.data = node_value
    elif node_value <= root.data:
        if root.left is None:
            root.left = BSTNode(node_value)
        else:
            insert_node(root.left, node_value)
    else:
        if root.right is None:
            root.right = BSTNode(node_value)
        else:
            insert_node(root.right, node_value)
    
    return "Node has been inserted"

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

new_bst = BSTNode(None)

print(insert_node(new_bst, 50))
print(insert_node(new_bst, 60))
print(insert_node(new_bst, 40))
print(insert_node(new_bst, 45))

preorder(new_bst)