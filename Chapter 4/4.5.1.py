class Stack:
    def __init__(self, list=None):
        if list is None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)

    def push(self, i):
        self.items.append(i)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def __sizeof__(self):
        return self.size

    def __str__(self):
        return ''.join(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def __sizeof__(self):
        return len(self.items)

    def __str__(self):
        return ''.join(self.items)


def process_explosion(items):
    s = Stack()
    explosion = 0
    explosion_items = []

    for item in items:
        if s.__sizeof__() >= 2 and s.peek() == item and s.items[-2] == item:
            explosion += 1
            while s.__sizeof__() >= 2 and s.peek() == item:
                n = s.pop()
            explosion_items.append(n)
        else:
            s.push(item)
    return s, explosion, explosion_items


def color_crush(n, m):
    m_items = list(reversed(m))
    m_stack, m_explosion, m_items = process_explosion(m_items)
    interference_items = []
    while not m_stack.isEmpty():
        interference_items.append(m_stack.pop())
    m_item = Queue()
    for item in m_items:
        m_item.enqueue(item)
    n_queue = Queue()
    for char in n:
        n_queue.enqueue(char)

    n_stack = Stack()
    n_explosion = 0
    interference_queue = Queue()
    for item in interference_items:
        interference_queue.enqueue(item)

    while not n_queue.isEmpty():
        item = n_queue.dequeue()
        if n_stack.__sizeof__() >= 2 and n_stack.peek() == item and n_stack.items[-2] == item:
            n_explosion += 1
            while n_stack.__sizeof__() >= 2 and n_stack.peek() == item:
                duplicate = n_stack.pop()
            if not interference_queue.isEmpty():
                n_explosion -= 1
                n_stack.push(duplicate)
                n_stack.push(m_item.dequeue())
                interference_queue.dequeue()
                n_stack.push(duplicate)
        else:
            n_stack.push(item)

    result_stack = Stack()
    while not n_stack.isEmpty():
        item = n_stack.pop()
        if result_stack.__sizeof__() >= 2 and result_stack.peek() == item and result_stack.items[-2] == item:
            n_explosion += 1
            while result_stack.__sizeof__() >= 2 and result_stack.peek() == item:
                result_stack.pop()
        else:
            result_stack.push(item)

    remaining_normal = ''.join(result_stack.items) if result_stack.items else "Empty"
    remaining_mirror = ''.join(reversed(m_stack.items)) if m_stack.items else "ytpmE"

    print("NORMAL :")
    print(len(result_stack.items))
    print(remaining_normal)
    print(f"{n_explosion} Explosive(s) ! ! ! (NORMAL)")
    print("------------MIRROR------------")
    print(": RORRIM")
    print(len(m_stack.items))
    print(f"{remaining_mirror}")
    print(f"(RORRIM) ! ! ! (s)evisolpxE {m_explosion}")


# Example usage:
n, m = input("Enter Input (Normal, Mirror) : ").split()
color_crush(n, m)
