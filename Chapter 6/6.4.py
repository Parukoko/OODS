def search(x, y, lst):
    if x < 0 or x >= len(lst) or y < 0 or y >= len(lst[0]):
        return False
    if lst[x][y] == 'E':
        return True
    if lst[x][y] in ('#', '*'):
        return False
    if not lst[x][y] == 'S':
        lst[x][y] = '*'
    # print(f"Visiting ({x}, {y})")
    if search(x+1, y, lst) or search(x, y+1, lst) or search(x, y-1, lst) or search(x-1, y, lst):
        return True

    lst[x][y] = '.'
    # print(f"Backtracking from ({x}, {y})")
    # for i in lst:
    #     print(''.join(i))
    return False

def findS(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 'S':
                return i, j

print("Enter the entire maze in one line. Use '.' for open cells, '#' for walls, 'S' for start, and 'E' for end.")
print("Separate each row with a comma (,).")
m = input("Enter the maze: ").split(',')
maze = [list(i) for i in m]
print("Your maze:")
for row in maze:
	print(''.join(row))
start = findS(maze)
if start:
	x, y = start
	# print(start)
	if search(x, y, maze):
		print("Solution found:")
		for row in maze:
			print(''.join(row))
	else:
		print("No solution found")
