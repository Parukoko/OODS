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
n, a = input("Enter Input : ").split('/')
q = Queue()
for i in n.split(' '):
	q.enqueue(i)
for i in a.split(','):
	if i.startswith('E'):
		_, num = i.split()
		q.enqueue(num)
	else:
		q.dequeue()
c = 0
repeated = []
for i in range(q.size()):
	k = i + 1
	for j in range(k, q.size()):
		if q.items[i] == q.items[j] and q.items[i] not in repeated:
			repeated.append(q.items[i])
if repeated == []:
	print("NO Duplicate")
else:
	print("Duplicate")
