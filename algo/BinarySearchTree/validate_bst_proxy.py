#o(n) time | o(d) space d = depth

def validateBST(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    isvalidLeft =  validateBSTHelper(tree.left, minValue, tree.value)   
    isvalidRight =  validateBSTHelper(tree.right, tree.value, maxValue) 
    return isvalidLeft and isvalidRight


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

print(validateBST(root))