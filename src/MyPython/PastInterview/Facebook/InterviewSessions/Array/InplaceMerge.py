"""
Inplace Merge

'a' and 'b' are both SORTED arrays of integers. Each contains 'n' sorted integers.
'a' has length 2*n, with the last n slots empty, and b has just n elements.
This method merges the elements from b into a, in place, without dynamic memory
allocation such that a is sorted and contains all the original integers from a and b. Optimize for speed.

void inplace_merge(int* a, int* b, int n);
Draw out an example with n = 4

Input
a = [1, 5, 6, 9, _, _, _, _ ]
b = [3, 4, 7, 10]

Output
a = [1, 3, 4, 5, 6, 7, 9, 10]
b = [3, 4, 7, 10]
"""


def insert(arr, pos_insert, key, last_empty):
	# Slide every element to the right
	for i in range(last_empty, pos_insert, -1):
		arr[i] = arr[i - 1]
	if arr[pos_insert] < key:
		arr[pos_insert + 1] = key
	elif arr[pos_insert] > key:
		arr[pos_insert + 1] = arr[pos_insert]
		arr[pos_insert] = key
	else:
		arr[pos_insert] = key


def binary_search(arr, low, high, key):
	if key > arr[high]:
		return high
	if high > low:
		while low < high:
			mid = low + (high - low) // 2
			if arr[mid] == key:
				return mid
			elif arr[mid] < key:
				low = mid + 1
			else:
				high = mid - 1
	if high == low:
		return low
	return -1


def inplace_merge_binary_search(a, b, n):
	last_a = n
	for i in range(len(b)):
		pos_insert = binary_search(a, 0, last_a - 1, b[i])
		insert(a, pos_insert, b[i], last_a)
		last_a += 1
	return a


def inplace_merge_swapping(a, b, n):
	first_empty = n
	for num in b:
		a[first_empty] = num
		b_num_idx = first_empty
		first_empty += 1
		for i in range(first_empty - 1, -1, -1):
			if a[i] > a[b_num_idx]:
				a[i], a[b_num_idx] = a[b_num_idx], a[i]
				b_num_idx -= 1
	return a




def inplace_merge_constant(a, b, n):
	a_pointer = b_pointer = n - 1
	last = len(a) - 1
	while a_pointer >= 0 and b_pointer >= 0:
		if b[b_pointer] >= a[a_pointer]:
			a[last] = b[b_pointer]
			b_pointer -= 1
		else:
			a[last] = a[a_pointer]
			a_pointer -= 1
		last -= 1
	return a


# a1 = [1, 5, 6, 9, 0, 0, 0, 0]
# b1 = [3, 4, 7, 10]
# n1 = 4
# # [1, 3, 4, 5, 6, 7, 9, 10]
#
# print(inplace_merge_binary_search(a1, b1, n1))
#
# a1 = [1, 5, 6, 9, 0, 0, 0, 0]
# b1 = [3, 4, 7, 10]
# n1 = 4
# print(inplace_merge_constant(a1, b1, n1))


a1 = [1, 5, 6, 9, 0, 0, 0, 0]
b1 = [3, 4, 7, 10]
n1 = 4
print(inplace_merge_swapping(a1, b1, n1))
