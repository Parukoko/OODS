class Stack:
	def __init__(self, list  = None):
		if list == None:
			self.items = []
		else:
			self.items = list
		self.size = len(self.items)
		self.temp = []
	def add(self, item):
		self.items.append(int(item))
		self.size += 1
	def pop(self):
		if self.isEmpty():
			return 0
		else:
			self.size -= 1
			return self.items.pop()
	def delete(self, item):
		self.temp.clear()
		item = int(item)
		to_delete = [x for x in self.items if x == item]
		self.temp.extend(to_delete)
		for x in to_delete:
			self.items.remove(x)
			self.size -= 1
			print(f"Delete = {x}")
	def ld(self, item):
		self.temp.clear()
		item = int(item)
		to_delete = [x for x in self.items if x < item]
		self.temp.extend(to_delete)
		for x in to_delete[::-1]:
			self.items.remove(x)
			self.size -= 1
			print(f"Delete = {x} Because {x} is less than {item}")
	def md(self, item):
		self.temp.clear()
		item = int(item)
		to_delete = [x for x in self.items if x > item]
		self.temp.extend(to_delete)
		for x in to_delete:
			self.items.remove(x)
			self.size -= 1
			print(f"Delete = {x} Because {x} is more than {item}")
	def isEmpty(self):
		return len(self.items) == 0

n = input("Enter Input : ").split(',')
s = Stack()
for i in n:
	if i.startswith('A'):
		_, num = i.split()
		s.add(num)
		print(f"Add = {num}")
	elif i.startswith('P'):
		if s.isEmpty():
			print("-1")
		else:
			popped = s.pop()
			print(f"Pop = {popped}")
	elif i.startswith('D'):
		_, num = i.split()
		if s.isEmpty():
			print("-1")
		else:
			deleted = s.delete(num)
			# print(f"Delete = {deleted}")
	elif i.startswith('LD'):
		_, num = i.split()
		if s.isEmpty():
			print("-1")
		else:
			s.ld(num)
	elif i.startswith('MD'):
		_, num = i.split()
		if s.isEmpty():
			print("-1")
		else:
			s.md(num)
print(f"Value in Stack = {s.items}")
