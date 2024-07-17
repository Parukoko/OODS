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
	def remove(self, item):
		self.items.remove(int(item))
		self.size -= 1
	def sizeof(self):
		return len(self.items)
	def isEmpty(self):
		return len(self.items) == 0
print("******** Parking Lot ********")
park_size,cars,action,c = input("Enter max of car,car in soi,operation : ").split(' ')
s = Stack()
for i in cars.split(','):
	if int(i) == 0:
		s.items = []
	else:
		s.add(int(i))
if action == 'arrive':
	if s.size >= int(park_size):
		print(f"car {c} cannot arrive : Soi Full")
	elif int(c) in s.items:
		print(f"car {c} already in soi")
	else:
		print(f"car {c} arrive! : Add Car {c}")
		s.add(int(c))
else:
	if s.isEmpty():
		print(f"car {c} cannot depart : Soi Empty")
	elif s.size > 0 and int(c) in s.items:
		s.remove(int(c))
		print(f"car {c} depart ! : Car {c} was remove")
	else:
		print(f"car {c} cannot depart : Dont Have Car {c}")
print(s.items)
