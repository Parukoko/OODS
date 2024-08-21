def GCD(a, b):
	if a == 0: return b
	if b == 0: return a
	elif a < b: return GCD(a, b % a)
	elif a > b: return GCD(a % b, b)
a, b = map(int, input("Enter Input : ").split(' '))
if a == 0 and b == 0:
	print("Error! must be not all zero.")
elif a > b:
	print(f"The gcd of {a} and {b} is : {GCD(abs(a), abs(b))}")
else:
	print(f"The gcd of {b} and {a} is : {GCD(abs(a), abs(b))}")
