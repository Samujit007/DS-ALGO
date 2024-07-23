def max_depth_of_binary_tree(root):
    return max_depth(root)

def max_depth(root):    
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = BST(1)
root.left = BST(2)
root.left.left = BST(4)
root.left.left.left = BST(8)
root.left.left.right = BST(9)
root.left.right = BST(5) 
root.right = BST(3)
root.right.left = BST(6)
root.right.right = BST(7)

print(max_depth_of_binary_tree(root))