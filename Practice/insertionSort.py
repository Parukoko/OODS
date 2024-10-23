def insertionSort(array, n):
	i = 1
	while i < n:
		element = array[i]
		ip = i
		while ip > 0 and array[ip-1] > element:
			array[ip] = array[ip-1]
			ip -= 1
		array[ip] = element
		i += 1
	return array
array = [9,4,5,1,0,7,8]
print(insertionSort(array,len(array)))
