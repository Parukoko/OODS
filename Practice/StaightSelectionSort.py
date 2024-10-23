def straightSelectionSort(array, n):
	last_idx = n - 1
	while last_idx > 0:
		biggest = array[0]
		big_idx = 0
		i = 1
		while i <= last_idx:
			if array[i] > biggest:
				biggest = array[i]
				big_idx = i
			i += 1
		array[big_idx], array[last_idx] = array[last_idx], array[big_idx]
		last_idx -= 1
	return array
array = [9,4,5,1,0,7,8]
print(straightSelectionSort(array,len(array)))
