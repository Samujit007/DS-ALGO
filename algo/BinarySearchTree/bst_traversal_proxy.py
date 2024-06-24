#o(n) time | o(n) space

def inOrderTraverse(tree, array): #L-N-R
    if tree is not None:
        inOrderTraverse(tree.left, array) #->tree.left.left till none
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array
#o(n) time | o(n) space
def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array) #->tree.left.left till none
        preOrderTraverse(tree.right, array)
    return array
#o(n) time | o(n) space
def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array) #->tree.left.left till none
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array

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

print(inOrderTraverse(root))
print(preOrderTraverse(root))
print(postOrderTraverse(root))