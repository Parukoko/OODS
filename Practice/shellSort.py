def shell(l, dincrement):
	n = len(l)
	for inc in dincrement:
		for i in range(inc, n):
			element = l[i]
			ip = i
			while ip > 0 and l[ip-inc] > element:
				l[ip] = l[ip-inc]
				ip -= inc
			l[ip] = element
	return l
array = [9,4,5,1,0,7,8]
increments = [4, 2, 1]
print(shell(array,increments))


