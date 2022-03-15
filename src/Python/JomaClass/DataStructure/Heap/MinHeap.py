class MinHeap:

	def __init__(self, a=[]):
		self.build_by_heapify(a)
		# self.build_by_insert(a)

	def build_by_insert(self, a):
		self.size = 0
		self.a = [0] * len(a)
		self.fill_up_heap(a)

	def build_by_heapify(self, a):
		self.a = a
		self.size = len(self.a)
		self.min_heapify_array()
		# self.min_heapify() # Another heapify implementation

	def left(self, i):
		return 2 * i + 1

	def right(self, i):
		return 2 * i + 2

	def parent(self, i):
		if i < 2:
			return 0
		else:
			return (i - 1) // 2  # instead of  (i - 2) / 2

	def min_heapify_aux(self, p):
		s = p  # assume that smallest is the current parent
		n = len(self.a)
		l = self.left(p)
		r = self.right(p)
		if l < n and self.a[l] < self.a[s]:  # if left child is smaller
			s = l
		if r < n and self.a[r] < self.a[s]:  # If right child is smaller
			s = r
		if s != p:  # if another smallest one was found (that is not the parent)
			# it means there is a new smallest one and therefore the order should be updated on the heap
			# These is base on the Min-Heap Order property, that parent nodes are always smaller or equal than children(s)
			self.a[p], self.a[s] = self.a[s], self.a[p]  # swap the smallest one with the parent (Fix Down / Sink the parent)
			self.min_heapify_aux(s)  # continue heapifying from the new smallest (new parent updated)

	def min_heapify(self):
		p = int((len(self.a) // 2) - 1)  # Calculate parents node indexes to call heapify on
		# Since leaf node don't have children, only parents are relevant to fix_down (sink)
		for i in range(p, -1, -1):  # Traverse parents node indexes in reverse
			self.min_heapify_aux(i)  # Call heapify on each parents

	def min_heapify_array(self):
		n = len(self.a)
		p = self.parent(n - 1)  # start with the parent of last node
		# Since leaf node don't have children, only parents are relevant to fix-down/sink
		for i in range(p, -1, -1):  # Traverse parents node in reverse and heapify each (used stop=-1 to included 0, the root)
			self.fix_down(i)  # Fix down (Sink) each parent

	def fill_up_heap(self, a):
		n = len(a)
		for i in range(n, 0, -1):
			self.insert(a.pop())  # insert in the new heap

	def insert(self, val):
		self.size += 1
		n = len(self.a)
		if self.size > n:  # array run out of space, it needs to resize
			self.a.append(val)
		else:
			self.a[self.size - 1] = val
		self.fix_up(self.size - 1)  # Fix up (Rise) to the top the last element inserted, if it is smaller

	def fix_up(self, i):  # Fix up (Rise) the smallest to the top of the heap
		if i == 0:  # If it is the root, there is nothing to Fix up because there are no parents
			return
		p = self.parent(i)  # Start with the parent of the current
		while p >= 0 and self.a[p] >= self.a[i]:
			self.a[i], self.a[p] = self.a[p], self.a[i]  # swap child node value with parent value
			if p == 0:  # if it is the root, there are no other parent to consider
				return
			else:  # Traverse to the next parent
				i = p  # curr becomes de parent
				p = self.parent(p)  # parent becomes the parent of the parent
		return

	def extract_min(self):
		n = self.size
		self.a[0], self.a[n - 1] = self.a[n - 1], self.a[0]  # Swap the current root with the last element(biggest)
		self.size -= 1  # Reduce size of the heap (not real size of the array)
		self.fix_down(0)  # Perform a Fix down (Sink) operation to the first element (root), currently the biggest
		# Since the root is now the biggest it will be replaced with the smallest
		# These is base on the Min-Heap Order property, that parent nodes are always smaller or equal than children(s)
		return self.a[self.size]

	def fix_down(self, i):  # Fix down (Sink) the biggest to the bottom of the heap (Sink)
		n = self.size
		while i < n - 1:
			j = self.left(i)  # Start with the left child of current
			if j >= n:  # If the left child index is out of bound
				break
			if j < n-1 and self.a[j] > self.a[j + 1]:  # If l child bigger than r, pick the r (r = l + 1) because is smaller
				j += 1
			if self.a[i] <= self.a[j]:  # If the curr is smaller or equal than the l (or r) child, there is nothing to fix down
				# These is base on the Min-Heap Order property, that parent nodes are always smaller or equal than children(s)
				break
			self.a[i], self.a[j] = self.a[j], self.a[i]  # Swap curr index i with smaller child found
			i = j  # update current to the smallest child

	def print_conceptual_heap(self):
		line = "Printing conceptual heap: ["
		for i in range(self.size):
			line += str(self.a[i])
			if i < self.size - 1:
				line += ", "
		line += "]"
		print(line)

	def print_actual_array(self):
		print("Printing actual array:    " + str(self.a))

#		3
#	   / \
#	  9   2
#    /\   /
#   1  4 5


# arr = [3, 9, 2, 1, 4, 5]
# print("Before heapify: ")  # [3, 9, 2, 1, 4, 5]
# print(arr)
# min_heap = MinHeap(arr)
#
# print("After heapify: ")
# min_heap.print_actual_array()     # [1, 2, 3, 5, 9, 4]
# min_heap.print_conceptual_heap()  # [1, 2, 3, 5, 9, 4]
#
# print("Extract Min: ")
# min_heap.extract_min()            # extract '1'
# min_heap.print_actual_array()     # [2, 4, 3, 5, 9, 1]
# min_heap.print_conceptual_heap()  # [2, 4, 3, 5, 9]
#
# print("Insert '10': ")
# min_heap.insert(10)
# min_heap.print_actual_array()     # [2, 4, 3, 5, 9, 10]
# min_heap.print_conceptual_heap()  # [2, 4, 3, 5, 9, 10]
#
# print("Insert '1': ")
# min_heap.insert(1)
# min_heap.print_actual_array()     # [1, 4, 2, 5, 9, 10, 3]
# min_heap.print_conceptual_heap()  # [1, 4, 2, 5, 9, 10, 3]
#
# print("Extract Min: ")
# min_heap.extract_min()            # extract '1'
# min_heap.print_actual_array()     # [2, 4, 3, 5, 9, 10, 1]
# min_heap.print_conceptual_heap()  # [2, 4, 3, 5, 9, 10]
#
# print("Insert '2': ")
# min_heap.insert(2)
# min_heap.print_actual_array()     # [2, 4, 2, 5, 9, 10, 3]
# min_heap.print_conceptual_heap()  # [2, 4, 2, 5, 9, 10, 3]
#
# print("Insert '1': ")
# min_heap.insert(1)
# min_heap.print_actual_array()     # [1, 2, 2, 4, 9, 10, 3, 5]
# min_heap.print_conceptual_heap()  # [1, 2, 2, 4, 9, 10, 3, 5]
#
# print("Insert '6': ")
# min_heap.insert(6)
# min_heap.print_actual_array()     # [1, 2, 2, 4, 9, 10, 3, 5, 6]
# min_heap.print_conceptual_heap()  # [1, 2, 2, 4, 9, 10, 3, 5, 6]
#
# print("Extract Min: ")
# min_heap.extract_min()            # extract '1'
# min_heap.print_actual_array()     # [2, 4, 2, 6, 9, 10, 3, 5, 1]
# min_heap.print_conceptual_heap()  # [2, 4, 2, 6, 9, 10, 3, 5]
#
# print("Extract Min: ")
# min_heap.extract_min()            # extract '2'
# min_heap.print_actual_array()     # [2, 4, 3, 6, 9, 10, 5, 2, 1]
# min_heap.print_conceptual_heap()  # [2, 4, 3, 6, 9, 10, 5]
#
# print("Extract Min: ")
# min_heap.extract_min()            # extract '2'
# min_heap.print_actual_array()     # [3, 4, 5, 6, 9, 10, 2, 2, 1]
# min_heap.print_conceptual_heap()  # [3, 4, 5, 6, 9, 10]
#
# print("Insert '11': ")
# min_heap.insert(11)
# min_heap.print_actual_array()     # [3, 4, 5, 6, 9, 10, 11, 2, 1]
# min_heap.print_conceptual_heap()  # [3, 4, 5, 6, 9, 10, 11]
#
# print("Insert '1': ")
# min_heap.insert(1)
# min_heap.print_actual_array()     # [1, 3, 5, 4, 9, 10, 11, 6, 1]
# min_heap.print_conceptual_heap()  # [1, 3, 5, 4, 9, 10, 11, 6]

# print(str((0 - 1) // 2))  # = > -1 - validated
# print(str((1 - 1) // 2))  # = > 0 - ok
# print(str((2 - 1) // 2))  # = > 0 - ok
# print(str((3 - 1) // 2))  # = > 1 - ok
# print(str((4 - 1) // 2))  # = > 1 - ok
# print(str((5 - 1) // 2))  # = > 2 - ok
# print(str((6 - 1) // 2))  # = > 2 - ok
# print(str((7 - 1) // 2))  # = > 3 - ok
# print(str((8 - 1) // 2))  # = > 3 - ok
