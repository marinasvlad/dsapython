class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        new_node = BSTNode(value)
        root = new_node    
    elif root.data is None:
        root.data = value
    else:
        if root.data <= value:
            insert_node(root.right, value)
        elif root.data > value:
            insert_node(root.left, value)

    return "Node as been inserted"

new_bst = BSTNode(None)

print(insert_node(new_bst, 50))
print(insert_node(new_bst, 60))
print(insert_node(new_bst, 40))
print(insert_node(new_bst, 45))