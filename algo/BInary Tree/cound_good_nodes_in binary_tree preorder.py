#BFS
def rec(head, max_val, count = 0):
    if head == None:
        return 0
    #     return res
    # if head.val >= max_val:
    #     max_val = head.val
    #     res = 1
    #     return res
    res = 1 if head.val >= max_val else 0
    max_val = max(head.val, max_val)
    res += rec(head.left, max_val, count)
    res += rec(head.right, max_val, count)
    return res

def count_good_nodes(root):
    return rec(root, root.val)
    # res.append(root.val)
    

class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root = BST(3)
root.left = BST(1)
root.left.left = BST(3)
# root.left.left.left = BST(6)
# root.left.right = BST(2)
root.right = BST(4)
root.right.left = BST(1)
root.right.right = BST(5)
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

print(count_good_nodes(root))
# [2,null,4,10,8,null,null,4]
