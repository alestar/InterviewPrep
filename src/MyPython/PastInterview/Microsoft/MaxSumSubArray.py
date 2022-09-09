"""
Example 1
Input: [-1, 2, 2,-3]
Output: 4
Explanation 2 + 2 = 4

Example 2:
Input: [-2, 1, -3 , 4, -1, 2, -1 , -5, 4]
output: 5
"""


def max_sum_sub_array(arr):

	if not arr:
		return 0

	max_sum = arr[0]
	curr_sum = 0
	for num in arr:
		curr_sum += num

		# If the current num makes the sum negative
		# Then, reset the curr_sum
		if curr_sum < 0:
			curr_sum = 0

			# Compare the curr num  with the max sum so far
			# In case is a bigger negative num, which will make the max_sum bigger
			max_sum = max(num, max_sum)

		# Otherwise, if the sum is positive
		else:
			# Compare the curr sum with the max sum seen so far
			max_sum = max(max_sum, curr_sum)
	return max_sum


print(max_sum_sub_array([]))
print(max_sum_sub_array([-1, 2, 2, -3]))
print(max_sum_sub_array([-1, -1, -2, -3]))
print(max_sum_sub_array([-5, -1, -2, -3]))
print(max_sum_sub_array([-1]))
print(max_sum_sub_array([-1, -2]))
print(max_sum_sub_array([5]))
print(max_sum_sub_array([0]))
print(max_sum_sub_array([-2, 1, -3, 4, -1, 2, -1, -5, 4]))

