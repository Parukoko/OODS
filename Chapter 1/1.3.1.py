def permute(nums):
	result = []
	lst = nums[:]
	last_item = lst.pop()
	for i in range(len(lst)+1):
		new_lst = lst[:]
		new_lst.insert(i, last_item)
		result.append(new_lst)
	return result

print("*** Fun with permute ***")
print("input :", end=" ")
a = list(map(int, input().split(',')))
print("Original Collection: ", a)
print("Collection of distinct numbers:")
print(permute(a))
