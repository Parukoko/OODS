class TreeNode():
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
			return TreeNode(data)
		if data < self.root.data:
			self.
