class Stack:
	def __init__(self, list  = None):
		if list == None:
			self.items = []
		else:
			self.items = list
		self.size = len(self.items)
	def add(self, item):
		self.items.append(int(item))
		self.size += 1
	def process_B(self):
		max_val = self.items[-1]
		count = 0
		for n in self.items[::-1]:
			if int(n) >= int(max_val):
				max_val == int(n)
				count += 1
				print(max_val)
			else:
				break
		print(count)

n = input("Enter Input : ").split(',')
s = Stack()
for i in n:
	if i.startswith('A'):
		_, num = i.split()
		s.add(num)
	if i.startswith('B'):
		s.process_B()

