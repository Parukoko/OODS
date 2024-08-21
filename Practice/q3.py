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
	def isEmpty(self):
		return len(self.items) == 0
n = list(input("input : ").split(","))
q = Queue()
left = 0
errror_input = 0
count = 0
for i in n:
	print(f"Step : {i}")
	if i.startswith('D'):
		if not q.isEmpty():
			for _ in range(int(i[1:])):
				if q.isEmpty():
					left += 1
				else:
					q.dequeue()

	elif i.startswith('E'):
		for i in range(count,i[1]+count-1):
			q.enqueue(i)
		count += i[1]
	else:
		errror_input += 1
print(f"Dequeue : {q.items}")
print(f"Error Dequeue : {left}")
print("--------------------")

