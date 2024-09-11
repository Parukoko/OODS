def printTree(root):
    tree_level = []
    temp = []
    tree_level.append(root)
    counter = 0
    height = root.getHeight() - 1
    number_of_elements = 2 ** (height + 1) - 1
    while counter <= height:
        removed = tree_level.pop(0)
        if len(temp) == 0:
            print_space(int(number_of_elements /
                            (2 ** (counter + 1))), removed)
        else:
            print_space(int(number_of_elements / (2 ** counter)), removed)
        if removed is None:
            temp.append(None)
            temp.append(None)
        else:
            temp.append(removed.left)
            temp.append(removed.right)
        if len(tree_level) == 0:
            print("\n")
            tree_level = temp
            temp = []
            counter += 1