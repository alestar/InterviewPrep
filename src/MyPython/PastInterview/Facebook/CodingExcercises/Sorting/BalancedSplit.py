"""

Balanced Split
Given an array of integers (which may include repeated integers),
determine if there's a way to split the array into two subsequences A and B such that the sum of the integers in both arrays is the same,
and all of the integers in A are strictly smaller than all of the integers in B.
Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.
Signature
bool balancedSplitExists(int[] arr)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if such a split is possible, and false otherwise.
Example 1
arr = [1, 5, 7, 1]
output = true
We can split the array into A = [1, 1, 5] and B = [7].
Example 2
arr = [12, 7, 6, 7, 6]
output = false
We can't split the array into A = [6, 6, 7] and B = [7, 12] since this doesn't satisfy the requirement that all integers in A are smaller than all integers in B.
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def binary_search(arr, target):
	lo, hi = 0, len(arr)-1

	while lo <= hi:
		mid = lo + (hi-lo)//2

		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			lo = mid + 1
		else:
			hi = mid - 1

	return -1

def balancedSplitExists(arr):
	# Write your code here
	arr = sorted(arr)

	running_sum = 0

	prefix_sums = []
	for n in arr:
		running_sum += n
		prefix_sums.append(running_sum)

	max_sum = prefix_sums[-1]
	if max_sum % 2 != 0:
		return False

	target = max_sum // 2

	found_index = binary_search(prefix_sums, target)
	if found_index == -1:
		return False

	return arr[found_index] < arr[found_index+1]



# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.


def printString(string):
	print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
	global test_case_number
	result = False
	if expected == output:
		result = True
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printString(expected)
		print(' Your output: ', end='')
		printString(output)
		print()
	test_case_number += 1


if __name__ == "__main__":
	arr_1 = [2, 1, 2, 5]
	expected_1 = True
	output_1 = balancedSplitExists(arr_1)
	check(expected_1, output_1)

	arr_2 = [3, 6, 3, 4, 4]
	expected_2 = False
	output_2 = balancedSplitExists(arr_2)
	check(expected_2, output_2)

	arr_3 = [1, 5, 7, 1]
	expected_3 = True
	output_3 = balancedSplitExists(arr_3)
	check(expected_3, output_3)

	arr_4 = [12, 7, 6, 7, 6]
	expected_4 = False
	output_4 = balancedSplitExists(arr_4)
	check(expected_4, output_4)

	# Add your own test cases here
