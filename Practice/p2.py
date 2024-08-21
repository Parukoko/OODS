class Stack:
	def __init__(self, lst=None) -> None:
		if lst is None:
			self.items = []
		else:
			self.items = lst
		self.size = len(self.items)
	def push(self, item):
		self.items.append(item)
		self.size += 1
	def pop(self, item):
		self.size -= 1
		return self.items.pop(item)
	def peek(self):
		if self.size > 0 :
			return self.items[-1]
		else: return None
n = list(map(str, input("Enter Input : ").split(',')))
s = Stack()
lst = []
for i in n:
	w, f = map(int, i.split(' '))
	while s and int(s.peek()[0]) < w and s.peek() is not None:
		lst.append(s.pop()[1])
	s.push((w,f))
for i in lst:
	print(i)
