class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def createLL(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def printLL(head):
    if not head:
        return "Empty"
    result = []
    current = head
    while current:
        result.append(str(current.value))
        current = current.next
    return " -> ".join(result)

def splitLL(head):
    if head is None or head.next is None:
        return head, None

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None
    return head, middle

def mergeLL(left, right):
    dummy = Node(0)
    current = dummy

    while left and right:
        if left.value <= right.value:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next

def mergeSortLL(head):
    if head is None or head.next is None:
        return head

    left, right = splitLL(head)
    left = mergeSortLL(left)
    right = mergeSortLL(right)

    return mergeLL(left, right)

inp = input("Enter unsorted Linked List: ").split()
head = createLL(inp)
print("Before:", printLL(head))
sorted_head = mergeSortLL(head)
print("After :", printLL(sorted_head))
