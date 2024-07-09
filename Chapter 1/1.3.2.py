print("*** Fun with permute ***")
print("input :", end=" ")
a = list(map(int, input().split(',')))
print("Original Cofllection: ", a)
print("Collection of distinct numbers:")
def insert_all_positions(lst, item):
    result = []
    for i in range(len(lst) + 1):
        new_lst = lst[:]
        new_lst.insert(i, item)
        result.append(new_lst)
    return result

def permute(nums):
    if len(nums) == 1:
        return [nums]
    last_item = nums[-1]
    prev_permutations = permute(nums[:-1])
    result = []
    for perm in prev_permutations:
        result.extend(insert_all_positions(perm, last_item))
    return result
result = permute(a)
reversed(result)
print(" ", end='')
print(result)
