def preOrder(root, level, res):
    if root is None:
        return
    if len(res) < level:
        res.append(root.val)
        preOrder(root.right, level+1, res)
        preOrder(root.left, level+1, res)

def binary_tree_right_side_view(root):
    res = []
    preOrder(root, 1, res)
    return res
 
class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root = BST(4)
root.left = BST(2)
root.left.left = BST(1)
root.left.right = BST(3) 
root.right = BST(7)

print(binary_tree_right_side_view(root))