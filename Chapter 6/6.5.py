def pyramid(n, i=0):
	if n == 0: return 0
	elif n < 0:
		print('_'*i+'#'*abs(n))
		return pyramid(n+1, i+1)
	else:
		print('_'*(n-1)+'#'*(i+1))
		return pyramid(n-1, i+1)
n = int(input("Enter Input : "))
if n == 0: print("Not Draw!")
pyramid(n)
