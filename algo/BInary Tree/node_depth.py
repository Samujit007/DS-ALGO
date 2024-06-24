#Recursion approach
#Time o(n) space o(h)
# def nodeDepth(tree):
#     depth = 0
#     return calcDepth(tree, depth)
   
# def calcDepth(tree,depth):
#     if tree == None:
#         return 0
#     return depth + calcDepth(tree.left, depth+1) + calcDepth(tree.right, depth+1)       

#===================Iterative=======================


def nodeDepth(tree):
    depth = 0
    stk = []
    stk.append({"node":tree,"node_depth": 0})
    while len(stk) >0:
        nodeInfo = stk.pop()
        node, node_depth = nodeInfo["node"], nodeInfo["node_depth"]
        if node is None:
            continue
        depth += node_depth
        stk.append({"node":node.left,"node_depth": node_depth+1})
        stk.append({"node":node.right,"node_depth": node_depth+1})
    return depth  

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

print(nodeDepth(root))