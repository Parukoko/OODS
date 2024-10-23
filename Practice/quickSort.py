def quickSort(l) :
	qSort(l, 0, len(l)-1)
def qSort(l, left, right):
	if left < right+1 :
		p = partition(l, left, right)
		qSort(l, left, p - 1)
		qSort(l, p + 1, right)
def partition(l, left, right):
	if left == right - 1 :
		if l[left] > l[right] :
			l[left],l[right] = l[right],l[left]
		return left
	c = (left + right)//2
	if l[left] > l[c] :
		l[left],l[c] = l[c],l[left]
	if l[right] < l[c] :
		l[c],l[right] = l[right],l[c]
	if l[right] < l[left] :
		l[left],l[right] = l[right],l[left]
	pivot = l[left]
	i, j = left + 1, right
	while i<j:
		while i<right and l[i]<=pivot:
			i += 1
		while j>left and l[j]>=pivot:
			j -= 1
		if i<j:
			l[i], l[j] = l[j], l[i]
	if left is not j:
		l[left], l[j] = l[j], pivot
	return j
l = [5,1,4,9,6,3,8,2,7,0]
quickSort(l)
print(l)
