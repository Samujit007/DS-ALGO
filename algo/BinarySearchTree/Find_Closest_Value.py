#recursive
#average Time: O(log(n)) | space: O(log(n))
#worst : If only one branch o(n) and | Space o(n)

# def findClosestValueInBST(tree, target):
#     return findClosestzHelper(tree, target, float("inf"))

# def findClosestzHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target-closest) > abs(target-tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestzHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestzHelper(tree.right, target, closest)
#     else:
#         return closest
#========================================================================
#iteratively
#average Time: O(log(n)) | Space: O(1)
#worst : If only one branch o(n) |Space o(1)
def findClosestValueInBST(tree, target):
    return findClosestzHelper(tree, target, float("inf"))

def findClosestzHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target-closest) > abs(target-currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
             currentNode = currentNode.right
        else:
            break
    return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
# tree = {
#   "nodes": [
#     {"id": "10", "left": "5", "right": "15", "value": 10},
#     {"id": "15", "left": "13", "right": "22", "value": 15},
#     {"id": "22", "left": None, "right": None, "value": 22},
#     {"id": "13", "left": None, "right": "14", "value": 13},
#     {"id": "14", "left": None, "right": None, "value": 14},
#     {"id": "5", "left": "2", "right": "5-2", "value": 5},
#     {"id": "5-2", "left": None, "right": None, "value": 5},
#     {"id": "2", "left": "1", "right": None, "value": 2},
#     {"id": "1", "left": None, "right": None, "value": 1}
#   ],
#   "root": "10"
# }
target = 11
print(findClosestValueInBST(root, target))