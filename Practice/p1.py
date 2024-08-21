class Stack:
	def __init__(self, lst=None):
		if lst is not None:
			self.items = lst
		else:
			self.items = []
		self.size = len(self.items)
	def push(self, item):
		self.items.append(item)
		self.size += 1
	def pop(self):
		self.size -= 1
		return self.items.pop()
n = list(map(str, input("Enter Input : ").split(',')))
s = Stack()
for i in n:
	if i.startswith('A'):
		_, num = i.split()
		s.push(num)
		print(f"Add = {num} and Size = {s.size}")
	else:
		a = s.pop()
		print(f"Pop = {a} and index = {s.size}")
print(f"Value in Stack =", end = ' ')
if s.items:
	print("Empty")
else:
	print(' '.join(s.items))
