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
p,t = input("Enter people and time : ").split(" ")
t = int(t)
cashier_1 = Queue()
cashier_2 = Queue()
main = Queue()
for i in p:
	main.enqueue(i)
count = 0
for i in range(1,t+1):
	if i % 3 == 1 and i != 1:
		cashier_1.dequeue()
	if i % 2 == 0 and not cashier_2.isEmpty():
		cashier_2.dequeue()
	if not main.isEmpty():
		if cashier_1.size() < 5:
			cashier_1.enqueue(main.items[0])
		else:
			cashier_2.enqueue(main.items[0])
		main.dequeue()

	print(f"{i} {main.items} {cashier_1.items} {cashier_2.items}")
