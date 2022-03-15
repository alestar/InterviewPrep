"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution(object):
	def two_sum_brute(self, nums, target):
		for i1, a in enumerate(nums):
			for i2, b in enumerate(nums):
				if a == b:
					continue
				if a + b == target:
					return [i1, i2]
		return []

	def two_sum_linear(self, nums, target):
		values = {}
		for i, num in enumerate(nums):
			complement = target - num
			if complement in values:
				return [i, values[complement]]
			values[num] = i
		return []


print(Solution().two_sum_brute([2, 7, 11, 15], 18))
print(Solution().two_sum_linear([2, 7, 11, 15], 18))
print(Solution().two_sum_brute([2, 7, 11, 15], 9))
print(Solution().two_sum_linear([2, 7, 11, 15], 9))
print(Solution().two_sum_brute([3, 2, 4], 6))
print(Solution().two_sum_linear([3, 2, 4], 6))
print(Solution().two_sum_brute([3, 3], 3))
print(Solution().two_sum_linear([3, 3], 3))
