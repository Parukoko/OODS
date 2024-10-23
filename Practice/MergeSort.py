def merge(l, left, right, rightEnd):
	start = left
	leftEnd = right-1
	result = []
	while left <= leftEnd and right <= rightEnd:
		if l[left] < l[right]:
			result.append(l[left])
			left += 1
		else:
			result.append(l[right])
			right += 1
	while left <= leftEnd:
		result.append(l[left])
		left += 1
	while right <= rightEnd:
		result.append(l[right])
		right += 1
	for i, val in enumerate(result):
		l[start + i] = val
def merge_sort(arr, left, right):
	if left < right:
		mid = (left + right) // 2
		merge_sort(arr, left, mid)
		merge_sort(arr, mid + 1, right)
		merge(arr, left, mid + 1, right)
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
