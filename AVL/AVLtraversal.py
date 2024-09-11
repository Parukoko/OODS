class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
        def __str__(self):
            return str(self.data)
        def setHeight(self):
                a = self.getHeight(self.left)
                b = self.getHeight(self.right)
                self.height = 1 + max(a,b)
                return self.height
        def getHeight(self, node):
            return -1 if node == None else node.height
        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)
    def __init__(self, root = None):
        self.root = None if root is None else root
    def add(self, data):
        self.root = self._add(self.root, data)
    def _add(self, root, data):
        if not root:
            return self.AVLNode(data)
        if data == root.data:
            if root.right is None:
                root.right = self.AVLNode(data)
            elif root.left is None:
                root.left = self.AVLNode(data)
        if  data < root.data:
            root.left = self._add(root.left, data)
        elif data > root.data:
            root.right = self._add(root.right, data)


        root.setHeight()
        balance = root.balanceValue()

        if balance < -1:
            if data < root.left.data:
                return self.rotateRightChild(root)
            elif data > root.left.data:
                root.left = self.rotateLeftChild(root.left)
                return self.rotateRightChild(root)
        if balance > 1:
            if data > root.right.data:
                return self.rotateLeftChild(root)
            elif data < root.right.data:
                root.right = self.rotateRightChild(root.right)
                return self.rotateLeftChild(root)
        return self._rebalance(root)

    def rotateLeftChild(self, root) :
         x = root.right
         root.right = x.left
         x.left = root
         root.setHeight()
         x.setHeight()
         return x

    def rotateRightChild(self, root) :
        x = root.left
        root.left = x.right
        x.right = root
        root.setHeight()
        x.setHeight()
        return x

    def postOrder(self):
         print("AVLTree post-order : ",end='')
         self._postOrder(self.root)
         print()\

    def _postOrder(self, node):
        if node:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node.data, end=' ')

    def printTree(self):
        self._printTree(self.root)
        print()

    def _printTree(self, node , level=0):
        if not node is None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self._printTree(node.left, level + 1)

    def _rebalance(self, root):
        balance = root.balanceValue()
        if balance < -1:
            if root.left.balanceValue() > 0:
                root.left = self.rotateLeftChild(root.left)
            return self.rotateRightChild(root)
        if balance > 1:
            if root.right.balanceValue() < 0:
                root.right = self.rotateRightChild(root.right)
            return self.rotateLeftChild(root)
        return root


avl1 = AVLTree()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AD":
        avl1.add(int(i[3:]))
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()
