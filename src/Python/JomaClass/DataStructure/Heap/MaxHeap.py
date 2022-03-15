class MaxHeap:

	def __init__(self, a=[]):
		self.build_by_heapify(a)
		#self.build_by_insert(a)

	def build_by_heapify(self, a):
		self.a = a
		self.size = len(self.a)
		self.max_heapify_array()
		# self.max_heapify()  # Another heapify implementation

	def build_by_insert(self, a):
		self.size = 0
		self.a = [0] * len(a)
		self.fill_up_heap(a)


	def left(self, i):
		return 2 * i + 1

	def right(self, i):
		return 2 * i + 2

	def parent(self, i):
		if i < 2:
			return 0
		else:
			return (i - 1) // 2  # instead of  (i - 2) / 2

	def max_heapify_aux(self, p):
		b = p  # assume that biggest is the current parent
		n = len(self.a)
		l_child = self.left(p)
		r_child = self.right(p)
		if l_child < n and self.a[l_child] > self.a[b]:  # if left child is bigger
			b = l_child
		if r_child < n and self.a[r_child] > self.a[b]:  # If right child is smaller
			b = r_child
		if b != p:  # if a different biggest one was found ( that is not the parent)
			# it means there is a new biggest one and therefore the order should be updated on the heap.
			# These is base on the Max-Heap Order property, that parent nodes are always bigger or equal to children(s)
			self.a[p], self.a[b] = self.a[b], self.a[p]  # swap the biggest one with the parent (Fix Down / Sink)
			self.max_heapify_aux(b)  # continue heapifying from the new biggest (new parent updated)

	def max_heapify(self):
		p = int((len(self.a) // 2) - 1)  # Calculate parents node indexes to call heapify on
		# Since leaf node don't have children, only parents are relevant to fix_down (sink)
		for i in range(p, -1, -1):  # Traverse parents node indexes in reverse
			self.max_heapify_aux(i)  # Call heapify on each parents

	def max_heapify_array(self):
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
		self.fix_up(self.size - 1)  # Fix up (Rise) to the top the last element inserted, if it is bigger

	def fix_up(self, i):  # Fix up (Rise) the biggest to the top of the heap
		if i == 0:  # If it is the root, there is nothing to Fix up because there are no parents
			return
		p = self.parent(i)  # Start with the parent of the current
		while p >= 0 and self.a[p] <= self.a[i]:
			self.a[i], self.a[p] = self.a[p], self.a[i]  # swap child node value with parent value
			if p == 0:  # if it is the root, there are no other parent to consider
				return
			else:  # Traverse to the next parent
				i = p  # curr becomes de parent
				p = self.parent(p)  # parent becomes the parent of the parent
		return

	def extract_max(self):
		n = self.size
		self.a[0], self.a[n - 1] = self.a[n - 1], self.a[0]  # Swap the current root with the last element(smaller)
		self.size -= 1  # Reduce size of the heap (not real size of the array)
		self.fix_down(0)  # Perform a Fix_down (Sink) operation to the first element (root), currently the smaller
		# Since the root is now the smaller it will be replaced with the biggest
		# These is base on the Max-Heap Order property, that parent nodes are always bigger or equal to children(s)
		return self.a[self.size]

	def fix_down(self, i):  # Fix down (Sink) the smallest to the bottom of the heap (Sink)
		n = self.size
		while i < n - 1:  # While curr is not the last element, because it does not have children to compare to not a leaf
			j = self.left(i)  # Start with the left child of current
			if j >= n:  # If the left child index is out of bound
				break
			if j < n-1 and self.a[j] < self.a[j + 1]:  # If l child smaller than r, pick the r (r = l + 1) because is bigger
				j += 1
			if self.a[i] >= self.a[j]:
				# If the curr is bigger or equal than the l (or r) child, there is nothing to fix down
				# These is base on the Max-Heap Order property, that parent nodes are always bigger or equal to children(s)
				break
			self.a[i], self.a[j] = self.a[j], self.a[i]  # Swap curr index i with bigger child found
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


arr = [3, 9, 2, 1, 4, 5]
#  k = 2 -> 1 Swap: 2 -> 5 = [3, 9, 5, 1, 4, 2]
#  k = 1 -> 0 Swap:  because 9 > 1 and 9 > 4 =  = [3, 9, 5, 1, 4, 2]
#  k = 0 -> 2 Swap: (3 -> 9) = [9, 3, 5, 1, 4, 2] ; (3 -> 4) = [9, 4, 5, 1, 3, 2]
#
print("Before heapify: ")  # [3, 9, 2, 1, 4, 5]
print(arr)
max_heap = MaxHeap(arr)

print("After heapify: ")
max_heap.print_actual_array()      # [9, 4, 2, 1, 3, 5] or [9, 4, 5, 1, 3, 2]
max_heap.print_conceptual_heap()   # [9, 4, 2, 1, 3, 5]

print("Extract Max: ")
max_heap.extract_max()            # extract '9'
max_heap.print_actual_array()     # [5, 4, 2, 1, 3, 9]
max_heap.print_conceptual_heap()  # [5, 4, 2, 1, 3]

print("Insert '10': ")
max_heap.insert(10)
max_heap.print_actual_array()     # [10, 4, 5, 1, 3, 2]
max_heap.print_conceptual_heap()  # [10, 4, 5, 1, 3, 2]

print("Insert '1': ")
max_heap.insert(1)
max_heap.print_actual_array()     # [10, 4, 5, 1, 3, 2, 1]
max_heap.print_conceptual_heap()  # [10, 4, 5, 1, 3, 2, 1]

print("Extract Max: ")
max_heap.extract_max()            # extract '10'
max_heap.print_actual_array()     # [5, 4, 1, 1, 3, 2, 10]
max_heap.print_conceptual_heap()  # [5, 4, 1, 1, 3, 2]

print("Insert '2': ")
max_heap.insert(2)
max_heap.print_actual_array()     # [5, 4, 2, 1, 3, 2, 1]
max_heap.print_conceptual_heap()  # [5, 4, 2, 1, 3, 2, 1]

print("Insert '1': ")
max_heap.insert(1)
max_heap.print_actual_array()     # [5, 4, 2, 1, 3, 2, 1, 1]
max_heap.print_conceptual_heap()  # [5, 4, 2, 1, 3, 2, 1, 1]

print("Insert '6': ")
max_heap.insert(6)
max_heap.print_actual_array()     # [6, 5, 2, 4, 3, 2, 1, 1, 1]
max_heap.print_conceptual_heap()  # [6, 5, 2, 4, 3, 2, 1, 1, 1]

print("Extract Max: ")
max_heap.extract_max()            # extract '6'
max_heap.print_actual_array()     # [5, 4, 2, 1, 3, 2, 1, 1, 6]
max_heap.print_conceptual_heap()  # [5, 4, 2, 1, 3, 2, 1, 1]

print("Extract Max: ")
max_heap.extract_max()            # extract '5'
max_heap.print_actual_array()     # [4, 3, 2, 1, 1, 2, 1, 5, 6]
max_heap.print_conceptual_heap()  # [4, 3, 2, 1, 1, 2, 1]

print("Extract Max: ")
max_heap.extract_max()            # extract '4'
max_heap.print_actual_array()     # [3, 1, 2, 1, 1, 2, 4, 5, 6]
max_heap.print_conceptual_heap()  # [3, 1, 2, 1, 1, 2]

print("Insert '11': ")
max_heap.insert(11)
max_heap.print_actual_array()     # [11, 1, 3, 1, 1, 2, 2, 5, 6]
max_heap.print_conceptual_heap()  # [11, 1, 3, 1, 1, 2, 2]

print("Insert '1': ")
max_heap.insert(1)
max_heap.print_actual_array()     # [11, 1, 3, 1, 1, 2, 2, 1, 6]
max_heap.print_conceptual_heap()  # [11, 1, 3, 1, 1, 2, 2, 1]

# print(str((0 - 1) // 2))  # = > -1 - validated
# print(str((1 - 1) // 2))  # = > 0 - ok
# print(str((2 - 1) // 2))  # = > 0 - ok
# print(str((3 - 1) // 2))  # = > 1 - ok
# print(str((4 - 1) // 2))  # = > 1 - ok
# print(str((5 - 1) // 2))  # = > 2 - ok
# print(str((6 - 1) // 2))  # = > 2 - ok
# print(str((7 - 1) // 2))  # = > 3 - ok
# print(str((8 - 1) // 2))  # = > 3 - ok
