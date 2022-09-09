class LinkedNode(object):

	def __init__(self, val, key):
		self.val = val
		self.key = key
		self.next = None
		self.prev = None

	def __repr__(self):
		return f"{self.val} -> {self.next.__repr__()}"


class LRUCache:

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.lookup = {}
		self.list = LinkedNode(0, 0)
		self.head = self.list.next
		self.tail = self.list.next

	def __repr__(self):
		return f"{self.head.__repr__()} [" + str(self.lookup) + "]"

	def remove_head_node(self):
		if not self.head:
			return
		prev = self.head
		self.head = self.head.next
		if self.head:
			self.head.prev = None
		del prev

	def append_new_node(self, new_node):
		"""  add the new node to the tail end
		"""
		if not self.tail:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.next = None
			new_node.prev = self.tail
			self.tail = self.tail.next

	def unlink_cur_node(self, node):
		""" unlink current linked node
		"""
		if self.head is node:
			self.head = node.next
			if node.next:
				node.next.prev = None
			return

		# removing the node from somewhere in the middle; update pointers
		prev, nex = node.prev, node.next
		prev.next = nex
		nex.prev = prev

	def get(self, key: int) -> int:
		if key not in self.lookup:
			return -1

		node = self.lookup[key]

		if node is not self.tail:
			self.unlink_cur_node(node)
			self.append_new_node(node)

		return node.val

	def put(self, key: int, value: int) -> None:
		if key in self.lookup:
			self.lookup[key].val = value
			self.get(key)
			return

		if len(self.lookup) == self.capacity:
			# remove head node and correspond key
			self.lookup.pop(self.head.key)
			self.remove_head_node()

		# add new node and hash key
		new_node = LinkedNode(val=value, key=key)
		self.lookup[key] = new_node
		self.append_new_node(new_node)


cache = LRUCache(5)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
cache.put(5, 5)
print(cache)
cache.put(6, 6)  # evicts '1'
print(cache)
print(cache.get(1))  # return -1,  since '1' was evicted prev
print(cache.get(4))  # update the '4' as the must recent
print(cache)
cache.put(7, 7)  # evicts '1'
print(cache.get(2))  # return -1,  since '2' was evicted prev
print(cache.get(3))  # update the '3' as the must recent
print(cache)


