class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value)
        while cur.next is not None:
            cur = cur.next
            s += " " + str(cur.value)
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value)
        while cur.previous is not None:
            cur = cur.previous
            s += " " + str(cur.value)
        return s

    def isEmpty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def addHead(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert(self, pos, item):
        new_node = Node(item)
        if pos < 0 and abs(pos) > self.size():
            self.addHead(item)
        if pos > 0 and abs(pos) > self.size():
            self.append(item)
        if pos < 0:
            current = self.tail
            count = 0
            while current.previous is not None and count > pos + 1:
                current = current.previous
                count -= 1
            if count == pos + 1:
                if current.previous is None:
                     self.addHead(item)
                else:
                    new_node.previous = current.previous
                    new_node.next = current
                    current.previous.next = new_node
                    current.previous = new_node

        if self.head is None:
            if pos == 0:
                self.head = self.tail = new_node
            # else:
            #     print("Out of Range")
            return

        if pos == 0:
            self.addHead(item)
            return

        current = self.head
        count = 0

        while current.next and count < pos - 1:
            current = current.next
            count += 1

        if count == pos - 1:
            if current.next is None:
                self.append(item)
            else:
                new_node.next = current.next
                new_node.previous = current
                current.next.previous = new_node
                current.next = new_node
        # else:
            # print("Out of Range")

    def search(self, item):
        h = self.head
        while h is not None:
            if h.value == item:
                return True
            h = h.next
        return False

    def index(self, item):
        index = 0
        h = self.head
        while h is not None:
            if h.value == item:
                return index
            h = h.next
            index += 1
        return -1

    def size(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

    def pop(self, pos):
        if pos < 0 or self.isEmpty():
            return "Out of Range"

        if pos == 0:
            if self.head.next is None:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None
            return "Success"

        current = self.head
        count = 0

        while current.next and count < pos:
            current = current.next
            count += 1

        if count == pos and current:
            if current.next is None:
                self.tail = current.previous
                if self.tail:
                    self.tail.next = None
            else:
                current.previous.next = current.next
                current.next.previous = current.previous
            return "Success"
        else:
            return "Out of Range"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format("Found" if L.search(i[3:]) else "Not Found", i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1} -> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        res = L.insert(int(data[0]), data[1])
        if res == "Out of Range":
            print(res)

print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
