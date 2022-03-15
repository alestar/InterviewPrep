def left(i):
	return 2 * i + 1


def right(i):
	return 2 * i + 2


def parent(i):
	if i < 2:
		return 0
	else:
		return (i - 1) // 2  # instead of  (i - 2) / 2


def fix_down(a, i, size):  # Fix down (Sink) the smallest to the bottom of the heap (Sink)
	n = size
	while i < n - 1:  # While curr is not the last element, because it does not have children to compare to not a leaf
		j = left(i)  # Start with the left child of current
		if j >= n:  # If the left child index is out of bound
			break
		if j < n-1 and a[j] < a[j + 1]:  # If l child smaller than r, pick the r (r = l + 1) because is bigger
			j += 1
		if a[i] >= a[j]:  # If the curr is bigger or equal than the l (or r) child, there is nothing to fix down
			# These is base on the Max-Heap Order property, that parent nodes are always bigger or equal to children(s)
			break
		a[i], a[j] = a[j], a[i]  # Swap curr index i with bigger child found
		i = j  # update current to the smallest child


def heap_sort(a):
	size = len(a)
	p = parent(size - 1)  # start with the parent of last node
	# Since leaf node don't have children, only parents are relevant to fix-down/sink
	for i in range(p, -1, -1):  # Traverse parents node in reverse and heapify each (used stop=-1 to included 0, the root)
		fix_down(a, i, size)  # Fix down (Sink) each parent
	print("Array Heapify:   " + str(a))
	while size > 1:
		a[0], a[size - 1] = a[size - 1], a[0]
		size -= 1
		fix_down(a, 0, size)


arr1 = [3, 6, 5, 8, 7, 2, 10, 1]
arr2 = [3, 6, 5, 8, 7, 2, 10, 1, 4]
arr3 = [18, 2, 15, 4, 30, 15, 19, 5, 6]
heap_sort(arr1)
print("Sorted Array #1: " + str(arr1))
heap_sort(arr2)
print("Sorted Array #2: " + str(arr2))
heap_sort(arr3)
print("Sorted Array #3: " + str(arr3))
