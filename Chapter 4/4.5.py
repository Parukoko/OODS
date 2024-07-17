class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return ''.join(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return ''.join(self.items)


def process_explosions(items):
    stack = Stack()
    explosions = 0

    for item in items:
        if len(stack) >= 2 and stack.peek() == item and stack.items[-2] == item:
            # Explosion detected
            explosions += 1
            while len(stack) >= 2 and stack.peek() == item:
                stack.remove()
        else:
            stack.add(item)

    return stack, explosions


def color_crush(normal_string, mirror_string):
    # Process mirror side
    mirror_items = list(reversed(mirror_string))
    mirror_stack, mirror_explosions = process_explosions(mirror_items)

    # Collect interference items from the mirror side
    interference_items = []
    while not mirror_stack.is_empty():
        interference_items.append(mirror_stack.remove())

    # Process normal side
    normal_queue = Queue()
    for char in normal_string:
        normal_queue.enqueue(char)

    normal_stack = Stack()
    normal_explosions = 0
    interference_queue = Queue()

    # Load the interference items into the interference queue
    for item in interference_items:
        interference_queue.enqueue(item)

    while not normal_queue.is_empty():
        item = normal_queue.dequeue()

        if len(normal_stack) >= 2 and normal_stack.peek() == item and normal_stack.items[-2] == item:
            # Explosion detected
            normal_explosions += 1
            while len(normal_stack) >= 2 and normal_stack.peek() == item:
                normal_stack.remove()

            # Apply interference item if available
            if not interference_queue.is_empty():
                interference_item = interference_queue.dequeue()
                # Insert interference item between the second and third element
                if len(normal_stack) >= 2 and normal_stack.items[-2] == item:
                    normal_stack.add(interference_item)
                else:
                    normal_stack.add(item)
            else:
                normal_stack.add(item)
        else:
            normal_stack.add(item)

    # Process any remaining items in the normal stack
    final_normal_stack = Stack()
    while not normal_stack.is_empty():
        item = normal_stack.remove()
        if len(final_normal_stack) >= 2 and final_normal_stack.peek() == item and final_normal_stack.items[-2] == item:
            normal_explosions += 1
            while len(final_normal_stack) >= 2 and final_normal_stack.peek() == item:
                final_normal_stack.remove()
        else:
            final_normal_stack.add(item)

    remaining_normal = ''.join(final_normal_stack.items) if final_normal_stack.items else "Empty"
    remaining_mirror = ''.join(mirror_stack.items) if mirror_stack.items else "Empty"

    print("NORMAL :")
    print(len(final_normal_stack.items))
    print(remaining_normal)
    print(f"{normal_explosions} Explosive(s) ! ! ! (NORMAL)")

    print("------------MIRROR------------")
    print(len(mirror_stack.items))
    print(f"RORRIM : {remaining_mirror}")
    print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_explosions}")


# Example input
n, m = input("Enter Input (Normal, Mirror) : ").split()
color_crush(n, m)
