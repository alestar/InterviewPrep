def quick_sort_range(a, first, last):
	if last <= first:   # Sub-group of one element, there is nothing left to sort
		return
	curr = last
	# First we partition the array (using curr pos index)
	# into elements that are less or equal than the first elem (the pivot), and
	# elements that are bigger than the pivot
	for i in range(last, first, -1):  # Partitioning loop
		if a[i] > a[first]:
			a[curr], a[i] = a[i], a[curr]  # Swap last position value with value that is bigger than the pivot
			curr -= 1  # move position to the left
	# Now we move the pivot to the front of the sub-group that are bigger than the pivot by:
	# swapping the pivot(first element) value with the value of were the current position of the partition begins
	a[first], a[curr] = a[curr], a[first]  # swap first element value with the value of the current index 'pos'
	# Finally, we recurse in both sub-groups
	quick_sort_range(a, first, curr - 1)
	quick_sort_range(a, curr + 1, last)


def quick_sort(a):
	n = len(a)
	quick_sort_range(a, 0, n - 1)


a = [10, 9, 8, 7, 6]
quick_sort(a)
print(a)
