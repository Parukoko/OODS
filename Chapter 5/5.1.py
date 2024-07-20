class Node:
    def __init__(self, value, next = None):
        self.value = value
        if next is None:
             self.next = None
        else:
            self.next = next
        self.size = 0

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.size += 1

    def addHead(self, item):
        h = Node(item)
        h.next = self.head
        self.head = h
        self.size += 1

    def search(self, item):
        h = self.head
        while h is not None:
            if h.value == item:
                return "Found"
            h = h.next
        return "Not Found"

    def index(self, item):
        index = 0
        h = self.head
        while h is not None:
            if h.value == item:
                return index
            h = h.next
            index += 1
        return "-1"

    def size(self):
        return self.size

    def pop(self, pos):
        if self.isEmpty():
            return "Out of Range"
        if pos < 0 or pos >= self.size:
            return "Out of Range"
        if pos == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(pos - 1):
                node = node.next
            node.next = node.next.next
        self.size -= 1
        return "Success"
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size, L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
