def quick_sort_range(arr, first, last):
	if last <= first:   # Sub-group of one element, there is nothing left to sort
		return

	# Select the Pivot Element as the leftest element of the array
	pivot = first

	# Select ref_pointer to point at the rightest element (since is going backwards)
	ref_pointer = last

	# First we partition the array using ref_pointer (Partitioning loop backwards)
	# by comparing elements that are less or equal than the the pivot, and elements that are bigger than the it.
	for i in range(last, first, -1):
		# If the curr comparing element is bigger than the pivot
		if arr[i] > arr[pivot]:
			# Swap the element in ref_pointer with the curr comparing element that is bigger than the pivot (move big element to the right)
			arr[ref_pointer], arr[i] = arr[i], arr[ref_pointer]

			# Move the ref_pointer pointer to the left to continue with the comparison
			ref_pointer -= 1
	# Go to the next comparing element

	# When completing comparing with all the elements,
	# the bigger elements than the pivot will have been swapped/moved to the right
	# Now, by swapping the pivot element with were the ref_pointer was left off,
	# A new partition will be created with a subgroup to the left(smaller) and a subgroup to the right(bigger)
	arr[pivot], arr[ref_pointer] = arr[ref_pointer], arr[pivot]

	# Now, the pivot has been moved to the front of the sub-group that are bigger than the it
	# Finally, recurse in both sub-groups of the new partition
	quick_sort_range(arr, first, ref_pointer - 1)
	quick_sort_range(arr, ref_pointer + 1, last)


def quick_sort(arr):
	quick_sort_range(arr, 0, len(arr) - 1)


arr1 = [10, 9, 8, 7, 6]
arr2 = [7, 9, 6, 10, 8]
print("Before sorting (arr1): " + str(arr1))
quick_sort(arr1)
print("After sorting (arr1)" + str(arr1))

print("Before sorting (arr2): " + str(arr2))
quick_sort(arr2)
print("After sorting (arr2)" + str(arr2))
