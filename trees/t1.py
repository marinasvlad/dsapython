class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level = 0):
        result = '   ' * level + str(self.data) + '\n'
        for child in self.children:
            result += child.__str__(level + 1)
        return result
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)
    
tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
fanta = TreeNode('Fanta', [])
cola = TreeNode('Cola', [])
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(fanta)
print(tree)