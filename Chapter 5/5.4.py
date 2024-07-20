class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_size(self):
        current = self.head
        i = 0
        while current:
            current = current.next
            i += 1
        return i

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def set_next(self, index1=int, index2=str):
        node1 = self.get_node_at_index(index1)
        if self.isEmpty():
            print("Error! {list is empty}")
        else:
            if node1 is None:
                 print("Error! {index not in length}:" ,index1)
                 return
            node2 = self.get_node_at_index(index2)
            if node2 is None:
                 self.append(index2)
                 node2 = self.get_node_at_index(index2)
                 self.next = node2
                 print("index not in length, append :",index2)
                 return
            node1.next = node2
            print(f"Set node.next complete!, index:value = {index1}:{node1.value} -> {index2}:{node2.value}")

    def get_node_at_index(self, index):
        current = self.head
        i = 0
        while current:
            if i == index:
                return current
            current = current.next
            i += 1
        return None

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def __str__(self) -> str:
        res = ""
        ptr = self.head
        while ptr:
            res += str(ptr.value) + "->"
            ptr = ptr.next
        res = res.strip("->")
        if len(res):
            return res
        else:
            return "Error! list is empty"
    def isEmpty(self):
        return self.get_size() == 0

# Testing
L = LinkedList()
inp = input("Enter input : ").split(',')

for i in inp:
    i = i.strip()  # Remove any extra spaces
    if i.startswith('A'):
        L.append(i[2:])
        print(L)
    elif i.startswith('S'):
        _, indices = i.split()
        index1, index2 = map(int, indices.split(':'))
        L.set_next(index1, index2)

if L.has_cycle():
    print("Found Loop")
else:
    print("No Loop")
    if L.isEmpty():
        print("Empty")
    else:
        print(L)
