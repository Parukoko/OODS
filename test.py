# s= '1'
# count = 0
# for i in s:
# 	count += ord(i)
# print(count%5)
def min(n):
	pn = n*2
	for num in range(pn, pn + 20):
		if num > 1:
			for i in range(2, int(num**0.5) + 1):
				if num % i == 0:
					break
			else:
				return num
print(min(5))
