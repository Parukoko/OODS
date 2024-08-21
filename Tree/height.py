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
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert(self.root, data)
	def _insert(self, node, data):
		if data < node.data:
			if node.left == None:
				node.left = Node(data)
			else:
				self._insert(node.left, data)
		else:
			if node.right == None:
				node.right = Node(data)
			else:
				self._insert(node.right, data)
	def printTree(self, node, level = 0):
		if node != None:
			self.printTree(node.right, level + 1)
			print('     '*level, node)
			self.printTree(node.left, level + 1)
	def print3Tree(self, node, level = 0, k = 0):
		if node is not None:
			self.print3Tree(node.right, level + int(1), k)
			if node.data > k:
				print(('     '*level), (int(node.data)*3))
			elif node.data <= k:
				print(('     '*level), int(node.data))
			self.print3Tree(node.left, level + int(1), k)
	def _printHeight(self, node):
		if node == None:
			return -1
		else:
			left = self._printHeight(node.right)
			right = self._printHeight(node.left)
			return max(left,right) + 1
	def height(self):
		return self._printHeight(self.root)
T = BST()
inp,k = input('Enter Input : ').split('/')
for i in inp.split():
	i = int(i)
	T.insert(i)
T.printTree(T.root)
print('--------------------------------------------------')
T.print3Tree(T.root, k=int(k))
