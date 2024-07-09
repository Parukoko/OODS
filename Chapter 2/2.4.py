lst = list(map(int, input("Enter Your List : ").split()))
n = []
seen = set()
if len(lst) <= 2:
	print("Array Input Length Must More Than 2")
else:
	for i in range(len(lst)):
		for j in range(i + 1, len(lst)):
			for k in range(j + 1, len(lst)):
				A, B, C = lst[i], lst[j], lst[k]
				if A + B + C == 5:
					triplet = sorted([A, B, C])
					if tuple(triplet) not in seen:
						seen.add(tuple(triplet))
						n.append(triplet)
	print(n)
