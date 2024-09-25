class Data:
	def __init__(self, key, value):
		self.key = key
		self.value = value
	def __str__(self):
		return "({0}, {1})".format(self.key, self.value)

class HashMap:
	def __init__(self, size, maxCollisions):
		self.size = int(size)
		self.maxCollisions = int(maxCollisions)
		self.bucket = [None] * self.size
	def get_index(self, key):
		index = sum(ord(char) for char in key)
		return index % int(self.size)
	def is_full(self):
		return all(self.bucket)
	def hashing_quadratic_probe(self, key, value):
		hashed_key = self.get_index(key)
		index = hashed_key
		if self.is_full():
			print('This table is full !!!!!!')
			return
		i = 0
		while i < self.maxCollisions:
			if self.bucket[hashed_key] is None:
				self.bucket[hashed_key] = Data(key, value)
				return
			else:
				print(f'collision number {i+1} at {index}')
				i += 1
				index = (hashed_key + pow(i,2)) % self.size
				if self.bucket[index] is None:
					self.bucket[index] = Data(key, value)
					return
		print('Max of collisionChain')
		# print('---------------------------')
	def __str__(self) -> str:
		result = ''
		for i in range(self.size):
			result += f"#{i+1}	{self.bucket[i]}\n"
		return result + "---------------------------"

print(" ***** Fun with hashing *****")
var, data = input("Enter Input : ").split('/')
tsize, maxCollision = var.split(' ')
hash = HashMap(tsize, maxCollision)
for pair in data.split(','):
	key, value = pair.split()
	hash.hashing_quadratic_probe(key, value)
	if hash.is_full():
		print(hash)
		print('This table is full !!!!!!')
		break
	else:
		print(hash)
