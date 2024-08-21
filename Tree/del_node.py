class Node:
	def __init__(self, data):
		self.data = int(data)
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.data)
class BinarySearchTree:
	def __init__(self) -> None:
		self.root = None
	def insert(self, val):
		val = int(val)
		if self.root is None:
			self.root = Node(val)
		else:
			self._insert(self.root, val)
		print("insert", val)
	def _insert(self, node, val):
		if val < node.data:
			if node.left == None:
				node.left = Node(val)
			else:
				self._insert(node.left, val)
		else:
			if node.right == None:
				node.right = Node(val)
			else:
				self._insert(node.right, val)
	def delete(self, r=0, val=0):
		print("delete", val)
		val = int(val)
		if self.root is None:
			print("Error! Not Found DATA")
		else:
			self.root = self._delete(self.root, val)
	def _delete(self, node, val):
		if node is None:
			print("Error! Not Found DATA")
			return
		if val < node.data:
			node.left = self._delete(node.left, val)
		elif val > node.data:
			node.right = self._delete(node.right, val)
		elif val == node.data:
			if node.left is None:
				return node.right
			elif node.right is None:
				return node.left
			temp = self._minValue(node.right)
			node.data = temp.data
			node.right = self._delete(node.right, temp.data)
		return node
	def _minValue(self, node):
		current = node
		while current:
			if current.left is None:
				break
			current = current.left
		return current
	def _search(self, node, val):
		if node is None:
			return False
		if node.data == val:
			return True
		elif node.data > val:
			return self._search(node.left, val)
		else:
			return self._search(node.right, val)
	def printTree90(self, node, level = 0):
		if node is not None:
			self.printTree90(node.right, level + 1)
			print('     ' * level, node)
			self.printTree90(node.left, level + 1)
tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
	if i.startswith('i'):
		tree.insert(i[2:].strip())
	if i.startswith('d'):
		tree.delete(val = i[2:].strip())
	tree.printTree90(tree.root)
