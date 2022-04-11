"""
Subarray with Target Sum or Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
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
	previous_sums = {0: -1}
	s = 0
	# Iterate through each element and calculate the sum to that point (idex)
	for index, n in enumerate(lst):

		# Add new element to the sum for each element
		s += n

		# Add the (sum, index) to the dict
		previous_sums[s] = index

		# If at any point, the complement of the current accumulated sum - target, was prev calculated and saved in the dict
		# Then, the index of the complement = previous_sums[s - target] will be the starting index of the continues sub-array
		# And the curr index will be the ending index of the sub-array
		if previous_sums.get(s - target):
			return lst[previous_sums[s - target] + 1: index + 1]
	return None


print(find_continuous_k_brute([1, 3, 2, 5, 7, 2], 14))
print(find_continuous_k_dict([1, 3, 2, 5, 7, 2], 14))
