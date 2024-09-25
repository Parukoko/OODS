def first_greater(l, r, lst, t):
	if l == r: return "No First Greater Value"
	elif lst[l] > t: return lst[l]
	else: return first_greater(l + 1, r, lst, t)
left, right = input('Enter Input : ').split('/')
left = list(map(int, left.split(' ')))
right = list(map(int, right.split(' ')))
for i in right:
	print(first_greater(0, len(left) - 1, sorted(left), i%1000000))
