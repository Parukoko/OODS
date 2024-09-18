def insertionSort(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr
l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
	Ans = "insertion sort"
	print("Extra Question : What is suitable sort algorithm?")
	print("   Your Answer : "+Ans)
else:
	l = list(map(int, l))
	arr = []
	sort = []
	lst = []
	for i,val in enumerate(l):
		arr.append(l[i])
		lst = l[:i+1:]
		sort = insertionSort(arr)
		if len(sort) % 2 == 0:
			mid = (len(sort)-1) // 2
			median = (sort[mid] + sort[mid + 1]) / 2
		else:
			mid = (len(sort) - 1) // 2
			median = sort[mid]
		print(f"list = {lst} : median =", "{:.1f}".format(median))
