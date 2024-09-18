def insertionSort(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr
def findSubset(n, lst):
	def backtrack(start, path, curr):
		if curr == n:
			valid.append(insertionSort(path))
			return
		if curr > n or start >= len(lst):
			return
		for i in range(start, len(lst)):
			backtrack(i+1, path + [lst[i]], curr + lst[i])
	valid = []
	backtrack(0, [], 0)
	for i in range(len(valid)):
		for j in range(len(valid) - 1):
			if len(valid[j]) > len(valid[j + 1]) or (len(valid[j]) == len(valid[j + 1]) and valid[j] > valid[j + 1]):
				valid[j], valid[j + 1] = valid[j + 1], valid[j]

	return valid
n, inp = input("Enter Input : ").split('/')
n = int(n)
lst = list(map(int, inp.split(' ')))
lst = insertionSort(lst)
result = findSubset(n, lst)
if result:
	for subset in result:
		print(subset)
else:
	print("No Subset")
