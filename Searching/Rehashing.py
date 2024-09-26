class Data:
	def __init__(self, key, value):
		self.key = key
		self.value = value
	def __str__(self):
		return "({0}, {1})".format(self.key, self.value)

class HashMap:
	def __init__(self, size, maxCollisions, threshold):
		self.size = int(size)
		self.maxCollisions = int(maxCollisions)
		self.threshold = int(threshold) / 100
		self.bucket = [None] * self.size
		self.capacity = 0
	def get_index(self, key):
		return key % self.size
	def is_full(self):
		return self.capacity >= self.size
	def min_double_prime_number(self, n):
		pn = n*2
		for num in range(pn, pn + 20):
			if num > 1:
				for i in range(2, int(num**0.5) + 1):
					if num % i == 0:
						break
				else:
					return num
	def rehash(self):
		old_size = self.size
		self.size = self.min_double_prime_number(self.size)
		old_bucket = self.bucket
		self.bucket = [None] * self.size
		self.capacity = 0
		for element in reversed(old_bucket):
			if element is not None:
				self.set_value(element, rehashed=True)
	def add_value(self, element, rehashed=False):
		print(f"Add : {element}")
		self.set_value(element, rehashed=False)
	def set_value(self, element, rehashed=False):
		if (self.capacity + 1) / self.size > self.threshold and not rehashed:
			print("****** Data over threshold - Rehash !!! ******")
			self.rehash()
		hashed_key = self.get_index(element)
		index = hashed_key
		i = 0
		while i < self.maxCollisions:
			if self.bucket[index] is None:
				self.bucket[index] = element
				self.capacity += 1
				return
			else:
				print(f'collision number {i+1} at {index}')
				i += 1
				index = (hashed_key + pow(i,2)) % self.size
			if i == self.maxCollisions:
				print('****** Max collision - Rehash !!! ******')
				self.rehash()
				self.set_value(element, rehashed=True)
				return

	def __str__(self) -> str:
		result = ''
		for i in range(self.size):
			result += f"#{i+1}	{self.bucket[i]}\n"
		return result + "----------------------------------------"

print(" ***** Rehashing *****")
var, data = input("Enter Input : ").split('/')
tsize, maxCollision, thres = var.split(' ')
hash = HashMap(tsize, maxCollision, thres)
print('Initial Table :')
print(hash)
for i in data.split(' '):
	hash.add_value(int(i))
	print(hash)
