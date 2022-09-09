"""
Subarray with Target Sum or Subarray Sum Equals K

Given an array of integers nums and an integer k, return the first sub-array that sums equals to target or k.

Example 1:
Input: nums = [4, 3, 5, 7, 8], target = 12
Output: [0, 2]
Explanation: 4 + 3 + 5 = 12. Although 5 + 7 = 12, [4, 3, 5] is the first subarray that sums up to 12.

Example 2:
Input: nums = [1, 2, 3, 4], target = 15
Output: None
Explanation: There is no such subarray that sums up to 15.
"""


def find_continuous_k_brute(lst, k):
	for start in range(len(lst)):
		s = 0
		for end in range(start, len(lst)):
			s += lst[end]
			if s == k:
				return lst[start:end + 1]
	return None


def find_continuous_k_dict(lst, target):
	# dictionary of the the (sum, index)
	sum_to_index = {0: -1}
	s = 0
	# Iterate through each element and calculate the sum to that point (index)
	for index, n in enumerate(lst):

		# Add new element to the sum for each element
		s += n

		# Add the (sum, index) to the dict
		sum_to_index[s] = index

		# If at any point, the complement of the current accumulated sum - target, was prev calculated and saved in the dict
		# Then, the index of the complement = sum_to_index[s - target] will be the starting index of the continuous sub-array
		# And the curr index will be the ending index of the continuous sub-array, whose sum equals to target.
		if sum_to_index.get(s - target):
			start_idx = sum_to_index[s - target] + 1
			end_index = index + 1
			return lst[start_idx: end_index]
	return None


print(find_continuous_k_brute([1, 3, 2, 5, 7, 2], 14))
print(find_continuous_k_dict([1, 3, 2, 5, 7, 2], 14))
