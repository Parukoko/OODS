class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.data)
class BST:
	def __init__(self):
		self.root = None
	def insert(self, data):
		self.root = BST._insert(self.root, data)
	def _insert(root, data):
		if root == None:
			return Node(data)
		else:
			if data < root.data:
				root.left = BST._insert(root.left, data)
			else:
				root.right = BST._insert(root.right, data)
		return root
	def printTree(self, node, level = 0):
		if node != None:
			self.printTree(node.right, level + 1)
			print('     '*level, node)
			self.printTree(node.left, level + 1)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
	T.insert(i)
T.printTree(T.root)
