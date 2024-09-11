class TreeNode(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.height = self.setHeight()
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height
    def getHeight(self, node = None):
        return -1 if node == None else node.height
    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)
    def __str__(self):
        return str(self.data)

class AVL_Tree(object):
    def __init__(self, root = None):
        self.root: TreeNode = None if root is None else root
    def insert(self, root, data):
        data = int(data)
        self.root = AVL_Tree._insert(root, data)
        return self.root
    def _insert(root, data):
        if not root:
            return TreeNode(data)
        if data < root.data:
            root.left = AVL_Tree._insert(root.left, data)
        else:
            root.right = AVL_Tree._insert(root.right, data)
        return AVL_Tree._rebalance(root, data)
    def setAllHeight(node: TreeNode):
        if node:
            node.setHeight()
            AVL_Tree.setAllHeight(node.left)
            AVL_Tree.setAllHeight(node.right)
    def rotateLeftChild(self, z):
        print("Left Left Rotation")
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.setHeight()
        y.setHeight()
        return y
    def rotateRightChild(self, z):
        print("Right Right Rotation")
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.setHeight()
        y.setHeight()
        return y
    def _rebalance(node: TreeNode, data):
        node.setHeight()
        balance = node.balanceValue()
        if balance > 1 and data < node.left.data:
            return AVL_Tree.rotateRightChild(AVL_Tree, node)
        if balance < -1 and data > node.right.data:
            return AVL_Tree.rotateLeftChild(AVL_Tree, node)
        if balance > 1 and data > node.left.data:
            node.left = AVL_Tree.rotateLeftChild(AVL_Tree, node.left)
            return AVL_Tree.rotateRightChild(AVL_Tree, node)
        if balance < -1 and data < node.right.data:
            node.right = AVL_Tree.rotateRightChild(AVL_Tree, node.right)
            return AVL_Tree.rotateLeftChild(AVL_Tree, node)
        return node

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

myTree = AVL_Tree()
root = None

print(" *** AVL Tree Insert Element ***")
data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("====================")
