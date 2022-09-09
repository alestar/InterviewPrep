"""
Given a sliced pizza with olives, what is the maximum number of olives that can be selected,
with the limitation that 2 adjacent slices cannot be selected.

Example 1:
Input: [3, 9, 8, 0, 100, 25, 10, 100]
Output: 209
"""

# def max_size_slices(arr):
# 	# @functools.lru_cache(None)
# 	def dp(i, j, k, cycle=0):
# 		if k == 1: return max(arr[i:j + 1])
# 		if j - i + 1 < k * 2 - 1: return -float('inf')
# 		return max(dp(i + cycle, j - 2, k - 1) + arr[j], dp(i, j - 1, k))
# 	return dp(0, len(arr) - 1, len(arr) // 3, 1)

import functools


class Solution:
	def max_size_slices(self, arr):
		n = len(arr) // 3

		@functools.lru_cache(None)
		def dp(i, j, k):
			if k == 1:
				return max(arr[i:j + 1])
			"""
			We have several cases:    
			case1: my_pizza, others, my_pizza, others
			case2: others, my_pizza, others, my_pizza
			case3: others, my_pizza, others
			case4: my_pizza, others, my_pizza
			it means if I need K pizza, case 1 and case 2 need 2k. case 3 need 2k+1, case4 needs 2k-1(minimum)
			If less than 2k-1, impossible
			"""
			if j - i + 1 < 2 * k - 1:
				return -float('inf')
			return max(dp(i + 2, j, k - 1) + arr[i], dp(i + 1, j, k))

		# Lots of posts pointed out why two cases here.
		return max(dp(0, len(arr) - 2, n), dp(1, len(arr) - 1, n))

	# DP without using early pruning.
	def max_size_slices_early_pruning(self, lst):
		n = len(lst) // 3

		@functools.lru_cache(None)
		def dp(i, j, k):
			"""
			the bottom case will be we only have two slice pizza left.
			if k==0: good, we already have enough pizza, return 0
			if k==1: good, return the maximum pizza
			if k==2: impossible.
			"""
			if j - i + 1 <= 2:
				if k == 0:
					return 0
				elif k == 1:
					return max(lst[i:j + 1])
				else:
					return -float('inf')
			return max(dp(i + 2, j, k - 1) + lst[i], dp(i + 1, j, k))

		# Lots of posts pointed out why two cases here.
		return max(dp(0, len(lst) - 2, n), dp(1, len(lst) - 1, n))


print(Solution().max_size_slices([3, 9, 8, 0, 100, 25, 10, 100]))  # 200, should be 209
