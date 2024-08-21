class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self is None:
            return Node(data)
        if data < self.data:
            self.left = Node.insert(self.left, data)
        else:
            self.right = Node.insert(self.right, data)
        return self

    def print_tree_prettily(self):
        all_line_list, *_ = self._create_pretty_tree()
        for line in all_line_list:
            print(line)

    def _create_pretty_tree(self):
        if self.left is None and self.right is None:
            data_line = f"{self.data}"
            data_width = len(str(self.data))
            height = 1
            root_index = 0
            return [data_line], data_width, height, root_index
        if self.right is None:
            all_line_list, total_data_width, height, root_index = self.left._create_pretty_tree()
            data_width = len(str(self.data))
            data_line = f"{' ' * (total_data_width + 1)}{self.data}"
            branch_line = f"{' ' * (root_index + self.left._peek_node_size())}{'_' * (total_data_width - root_index - self.left._peek_node_size())}/{' ' * data_width}"
            shifted_all_line_list = [line + (' ' * (data_width + 1)) for line in all_line_list]
            return [data_line, branch_line] + shifted_all_line_list, total_data_width + data_width + 1, height + 2, total_data_width + 1
        if self.left is None:
            all_line_list, total_data_width, height, root_index = self.right._create_pretty_tree()
            data_width = len(str(self.data))
            data_line = f"{self.data}{' ' * (total_data_width + 1)}"
            branch_line = f"{' ' * data_width}\\{'_' * (root_index)}{' ' * (total_data_width - root_index)}"
            shifted_all_line_list = [(' ' * (data_width + 1)) + line for line in all_line_list]
            return [data_line, branch_line] + shifted_all_line_list, total_data_width + data_width + 1, height + 2, 0

        left_all_line_list, left_total_data_width, left_height, left_root_index = self.left._create_pretty_tree()
        right_all_line_list, right_total_data_width, right_height, right_root_index = self.right._create_pretty_tree()
        data_width = len(str(self.data))
        data_line = f"{' ' * (left_total_data_width + 1)}{self.data}{' ' * (right_total_data_width + 1)}"
        branch_line = f"{' ' * (left_root_index + self.left._peek_node_size())}{'_' * (left_total_data_width - left_root_index - self.left._peek_node_size())}/{' ' * data_width}\\{'_' * (right_root_index)}{' ' * (right_total_data_width - right_root_index)}"
        if left_height > right_height:
            right_all_line_list += [' ' * (right_total_data_width)] * (left_height - right_height)
        elif left_height < right_height:
            left_all_line_list += [' ' * (left_total_data_width)] * (right_height - left_height)
        full_line_list = [data_line, branch_line] + [left_line + (' ' * (data_width + 2)) + right_line for left_line, right_line in zip(left_all_line_list, right_all_line_list)]
        return full_line_list, left_total_data_width + data_width + right_total_data_width + 2, max(left_height, right_height) + 2, left_total_data_width + 1

    def _peek_node_size(self):
        return len(str(self.data))

inp = map(int, input('Enter input: ').split())
root = None
for i in inp:
    root = Node.insert(root, i)
root.print_tree_prettily()
