class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
	def insert(self, data):
		if self is None:
			return Node(data)
		if data < self.data:
			self.left = Node.insert(self.left, data)
		else:
			self.right = Node.insert(self.right, data)
		return self
	def display(self):
		lines, *_ = self._display()
		for line in lines:
			print(line)
	def _display(self):
		if self.right is None and self.left is None:
			line = '%s' % self.data
			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle
		if self.right is None:
			lines, n, p, x = self.left._display()
			s = '%s' % self.data
			u = len(s)
			first_line = (n + 1) * ' ' + s
			second_line = u * ' ' + (n - u) * '_' + '/'
			shifted_lines = [line + (u + 1) * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u + 1, p + 2, (n + u + 1) // 2
		if self.left is None:
			lines, n, p, x = self.right._display()
			s = '%s' % self.data
			u = len(s)
			first_line = s
			second_line = u * ' ' + '\\' + (x - 1) * '_'
			shifted_lines = [(u + 1) * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u + 1, p + 2, (u + 1) // 2
		left, n, p, x = self.left._display()
		right, m, q, y = self.right._display()
		s = '%s' % self.data
		u = len(s)
		first_line = (n + 1) * ' ' + s + (m - y) * ' '
		second_line = n * ' ' + (x + 1) * '_' +  '/' + (u) * ' ' + '\\' + (y + 1) * '_'
		if p < q:
			left += [n * ' '] * (q - p)
		elif p > q:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + (u + 2) * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u + 2, max(p, q) + 2, (n + u + m + 2)// 2
inp = map(int, input('Enter input: ').split())
root = None
for i in inp:
	if root is None:
		root = Node(i)
	else:
		root.insert(i)
Node.display(root)
