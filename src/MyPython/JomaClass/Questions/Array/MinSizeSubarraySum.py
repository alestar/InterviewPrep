"""
Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""


class Solution(object):
	def min_sub_array(self, k, nums):
		left_idx = right_idx = 0
		curr_sum = 0
		min_len = float('inf')

		# Iterate from the right_idx to the end of the array (since all combination must be check)
		# and determine which index has to move to the right
		# depending if the curr_sum is bigger or smallest than the target sum k.
		# This is call as a sliding window mechanism (opening-closing the window)
		while right_idx < len(nums):

			# Add elements to the curr_sum
			curr_sum += nums[right_idx]

			# When at some point the curr_sum becomes bigger than the target sum
			# Then proceed to move the left index and exclude left elements (closing the windows)
			# until curr_sum becomes less or equal target sum
			while curr_sum >= k:
				min_len = min(min_len, right_idx - left_idx + 1)
				curr_sum -= nums[left_idx]
				left_idx += 1

			# Otherwise continue moving the right_idx to the right (opening the window)
			right_idx += 1

		# If the value of min_len was not altered, error out
		if min_len == float('inf'):
			return 0
		return min_len


print(Solution().min_sub_array(7, [2, 3, 1, 2, 4, 3]))  # 2


