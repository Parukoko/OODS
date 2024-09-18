def BubbleSort(lst):
	n = len(lst)
	for i in range(n):
		swapped = False
		for j in range(0, n-i-1):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
				swapped = True
		if swapped == False:
			break
inp = list(map(int, input("Enter Input : ").split(' ')))
BubbleSort(inp)
print(inp)
