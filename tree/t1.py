class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def add_child(self, tree_node):
        self.children.append(tree_node)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.add_child(cold)
tree.add_child(hot)

print(tree)

tea = TreeNode('Tea', [])
coffe = TreeNode('Coffe', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])

cold.add_child(fanta)
cold.add_child(cola)
hot.add_child(tea)
hot.add_child(coffe)

print(tree)
