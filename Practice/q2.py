class Queue:
	def __init__(self):
		self.items = []
	def enqueue(self, item: str):
		self.items.append(item)
	def dequeue(self):
		if self.items:
			return self.items.pop(0)
	def _size(self):
		return len(self.items)

n = input("Enter people : ")
main = Queue()
c1 = Queue()
c2 = Queue()
for i in n:
	print(i)
	main.enqueue(i)

for i in range(1,len(n)+1):
	if i % 3 == 1 and i != 1:
		c1.dequeue()
	if i % 2 == 0 and i != 1:
		c2.dequeue()
	if main.items:
		if c1._size() >= 5:
			c2.enqueue(main.items[0])
		else:
			c1.enqueue(main.items[0])
		main.dequeue()
	print("{0} {1} {2} {3}".format(i,main.items, c1.items, c2.items))
