def maxIdx(lst, i, j):
	if i == j:
		return i
	k = maxIdx(lst, i+1, j)
	return (i if lst[i] > lst[k] else k)
def StraightSelectionSort(lst, idx):
	if idx < 0:
		return -1
	k = maxIdx(lst, 0, idx)
	if k != idx:
		lst[k], lst[idx] = lst[idx], lst[k]
		print(f"swap {lst[k]} <-> {lst[idx]} : {lst}")
	StraightSelectionSort(lst, idx - 1)
inp = list(map(int, input("Enter Input : ").split()))
n = len(inp)
StraightSelectionSort(inp, n-1)
print(inp)
