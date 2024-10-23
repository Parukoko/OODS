def bubbleSort(array,n):
	last_idx = n - 1
	while last_idx >= 0:
		swapped = False
		i = 0
		while i < last_idx:
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				swapped = True
			i += 1
		if not swapped:
			break
		last_idx -= 1
	return array
array = [9,4,5,1,0,7,8]
print(bubbleSort(array,len(array)))
