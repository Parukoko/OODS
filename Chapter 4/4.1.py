class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def enqueue(self, item):
		self.items.append(item)
	def dequeue(self):
		return self.items.pop(0)
	def size(self):
		return len(self.items)
	def peek(self):
		return self.items[0]
n = input("Enter Input : ").split(',')
q = Queue()
for i in n:
	if i.startswith('E'):
		_, num = i.split()
		q.enqueue(num)
		print(q.size())
	else:
		if q.isEmpty():
			print('-1')
		else:
			print(q.peek(), '0')
			q.dequeue()
if q.isEmpty():
	print('Empty')
else:
	for i in q.items:
		print(i,end=' ')
