class Node:
	def __init__(self, value=None, prev=None, next=None):
		self._value = value
		self._prev = prev
		self._next = next
class DoublyLinkedList:
	def __init__(self) -> None:
		self._head = None
		self._tail = None
	def addHead(self, item):
		new_node = Node(item)
		if self._head is None:
			self._head = self._tail = new_node
		else:
			self._head._prev = new_node
			new_node._next = self._head
			self._head = new_node
	def append(self, item):
		new_node = Node(item)
		if self._head is None:
			self._head = self._tail = new_node
		else:
			self._tail._next = new_node
			new_node._prev = self._tail
			self._tail = new_node
	def insert(self, pos, item):
		if self._head is None:
			return "List is Empty"
		if pos == 0:
			self.addHead(item)
		current = self._head
		index = 0
		while current is not None:
			if index == pos:
				new_node = Node(item)
				new_node._prev = current._prev
				new_node._next = current
				current._prev._next = new_node
				current._next._prev = new_node
				return
			current = current._next
			index += 1
		if index == pos:
			self.append(item)
