def bon(w):
	for i in w:
		if w.count(i) > 1:
			return (ord(i) - 96)*4
secretCode = input("Enter secret code : ")
print(bon(secretCode))
