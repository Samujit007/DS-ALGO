#BFS
def rec(head, res):
    if head == None:
        return
    if head and head.left == None and head.right == None:
        res.append(head.val)
    rec(head.left, res)
    rec(head.right, res) 

def binary_tree_leaf_similer(root1, root2):
    res1 = []
    res2 = []
    rec(root1, res1)
    rec(root2, res2)
    return res1 == res2

class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root1 = BST(1)
root1.left = BST(2)
root1.right = BST(3)
root2 = BST(1)
root2.left = BST(2)
root2.right = BST(3)

print(binary_tree_leaf_similer(root1, root2))