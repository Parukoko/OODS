class Stack:
	def __init__(self, list  = None):
		if list == None:
			self.items = []
		else:
			self.items = list
		self.size = len(self.items)

	def push(self, i):
		self.items.append(i)
		self.size += 1
	def pop(self):
		self.size -= 1
		return self.items.pop()
	def peek(self):
		if self.isEmpty():
			return None
		return self.items[-1]
	def isEmpty(self):
		return len(self.items) == 0
	def sizeof(self):
		return self.size
n = input("Enter Input : ").split(',')
s = Stack()
for i in n:
	if i.startswith('A'):
		_, num = i.split()
		s.push(num)
		print(f"Add = {num} and Size = {s.sizeof()}")
	else:
		if s.isEmpty():
			print("-1")
		else:
			print(f"Pop = {s.peek()} and Index = {s.sizeof() - 1}")
			s.pop()
print("Value in Stack = ",end='')
if s.isEmpty():
	print('Empty')
else:
	print(' '.join(s.items))
