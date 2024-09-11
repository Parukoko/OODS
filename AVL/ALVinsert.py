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
        root.setHeight()
        return AVL_Tree._rebalance(root)

    def rotateLeftChild(node: TreeNode):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        node.setHeight()
        newRoot.setHeight()
        return newRoot

    def rotateRightChild(node: TreeNode):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        node.setHeight()
        newRoot.setHeight()
        return newRoot

    def _rebalance(node: TreeNode):
        balance = node.balanceValue()
        if balance == -2:
            print("Not Balance, Rebalance!")
            if node.right.balanceValue() == 1:
                node.right = AVL_Tree.rotateLeftChild(node.right)
            node = AVL_Tree.rotateRightChild(node)
        elif balance == 2:
            print("Not Balance, Rebalance!")
            if node.left.balanceValue() == -1:
                node.left = AVL_Tree.rotateRightChild(node.left)
            node = AVL_Tree.rotateLeftChild(node)
        return node

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

myTree = AVL_Tree()
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")
