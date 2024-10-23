from math import log2, floor
def print90(h, i, max_i):
	if i < max_i:
		indent = floor(log2(i+1))
		print90(h, (i*2)+2, max_i)
		print('   ' * indent, h[i])
		print90(h, (i*2)+1, max_i)
def insertMinHeap(h, i):
	print('insert', h[i], 'at index', i, end='              ')
	print(h)
	element = h[i]
	fi = (i-1)//2
	while i > 0 and element < h[fi]:
		h[i] = h[fi]
		i = fi
		fi = (i-1)//2
	h[i] = element
def delMinHeap(h, last):
	print('del', h[0], 'at index', last, end='              ')
	print(h)
	element = h[last]
	h[last] = h[0]
	hole = 0
	ls = hole*2 + 1
	found = False
	while ls < last and not found:
		rs = ls if ls + 1 >= last else ls + 1
		min_child = ls if h[ls] < h[rs] else rs
		if h[min_child] < element:
			h[hole] = h[min_child]
			hole = min_child
			ls = hole*2 + 1
		else:
			found = True
	h[hole] = element
h = [13,14,16,24,21,19,68,65,26,32,31]
for i in range(1, len(h)):
	insertMinHeap(h,i)
	print(h)
	print90(h, 0, i)
	print('-----------------\n')

for last in range(len(h)-1, -1, -1):
	delMinHeap(h, last)
	print(h)
	print90(h, 0, last)
	print('------------------\n')

