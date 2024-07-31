def search_in_binary_search_tree(root, val):
    while root is not None:
        if val == root.value:
            return root
        elif val > root.value:
            root = root.right
        else:
            root = root.left    
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = BST(4)
root.left = BST(2)
root.left.left = BST(1)
root.left.right = BST(3) 
root.right = BST(7)
val = 2
print(search_in_binary_search_tree(root, val))