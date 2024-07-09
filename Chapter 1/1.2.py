print("*** multiplication or sum ***")
print("Enter num1 num2 :", end = " ")
a = list(map(int, input().split(' ')))
if a[0]*a[1] > 1000:
	print("The result is" ,a[0]+a[1])
else:
	print("The result is" ,a[0]*a[1])
