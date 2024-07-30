def longest_zigzag_path(root):   
    maxPath = 0
    def rec(head, step, go_left):
        nonlocal maxPath
        if head == None:
            return
        maxPath = max(maxPath, step)
        if go_left:
            rec(head.left, step + 1, False)
            rec(head.right, 1, True)
        else:
            rec(head.left, 1, False)
            rec(head.right, step+1, True)
    rec(root, 0, True)#Exploring left
    rec(root, 0, False)#Exploring right
    return maxPath



class BST:
    maxPath = 0
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = BST(1)
root.right = BST(1)
root.right.left = BST(1)
root.right.right = BST(1)
root.right.right.left = BST(1)
root.right.right.right = BST(1)
root.right.right.left.right = BST(1)
root.right.right.left.right.right = BST(1)

# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

print(longest_zigzag_path(root))
# [2,null,4,10,8,null,null,4]
