def operator(c):
	if c == '^':
		return 3
	elif c == '/' or c == '*':
		return 2
	elif c == '+' or c == '-':
		return 1
	else:
		return -1
def associative_operator(c):
	if c == '^':
		return 'R'
	return 'L'
def infix2postfix(s):
	result = []
	stack = []
	for i in range(len(s)):
		c = s[i]
		if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
			result.append(c)
		elif c == '(':
			stack.append(c)
		elif c == ')':
			while stack and stack[-1] != '(':
				result.append(stack.pop())
			stack.pop()
		else:
			while stack and ((operator(c) < operator(stack[-1])) or (operator(c) == operator(stack[-1]) and associative_operator(c) == 'L')):
				result.append(stack.pop())
			stack.append(c)
	while stack:
		result.append(stack.pop())
	print(''.join(result))
a = input("Enter Infix : ")
print("Postfix : ",end='')
infix2postfix(a)
