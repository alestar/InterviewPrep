"""
Rotate Array

This problem is to rotate a given array to the right by n steps.

For example:
Given [1, 2, 3] and n = 1, you should return [3, 1, 2]
Each step, the last element in the array is moved to the front of the array, and the rest are shifted right.

Another example:
Given [1, 2, 3, 4, 5] and n = 3, you should return [3, 4, 5, 1, 2]
"""


def rotate_array(arr, rot_f):
	n = len(arr)
	res = [0] * n

	for i in range(n):
		pos = (i + rot_f) % n
		res[pos] = arr[i]
	return res


def rotate_array_const_space(arr, rot_f):
	if not arr:
		return None
	n = len(arr)
	pos = 0
	for i in range(n):
		pos = (pos + rot_f) % n
		old = arr[pos]
		arr[pos] = new
		new = old
	return arr


# print(rotate_array([1, 2, 3, 4, 5], 3))  # [3, 4, 5, 1, 2]
# print(rotate_array([1, 2, 3, 4, 5], -3))  # [4, 5, 1, 2, 3]
# print(rotate_array([1, 2, 3, 4, 5], 0))  # [1, 2, 3, 4, 5]
# print(rotate_array([], -3))  # []

print(rotate_array_const_space([1, 2, 3, 4, 5], 3))  # [3, 4, 5, 1, 2]
print(rotate_array_const_space([1, 2, 3, 4, 5], -3))  # [4, 5, 1, 2, 3]
print(rotate_array_const_space([1, 2, 3, 4, 5], 0))  # [1, 2, 3, 4, 5]
print(rotate_array_const_space([], -3))  # []


