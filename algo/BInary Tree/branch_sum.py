#iteratively
#average Time: O(log(n)) | Space: O(1)
#worst : If only one branch o(n) |Space o(1)
def branchSum(tree):
    sum = []
    calculateSum(tree, 0, sum)
    return sum

def calculateSum(tree, runningSum, sumList):
    if tree is None:
        return
    newRunningSum = runningSum + tree.value
    if tree.left is None and tree.right is None:
        sumList.append(newRunningSum)
        return sumList
    calculateSum(tree.left, newRunningSum, sumList) 
    calculateSum(tree.right, newRunningSum, sumList) 


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

print(branchSum(root))