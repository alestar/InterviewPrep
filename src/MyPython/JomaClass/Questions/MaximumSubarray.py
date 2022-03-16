"""
Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution:

	# Since not all the numbers in the array are positive,
	# the max sum possible value for a contiguous subarray could vary by including (adding or subtracting to the curr_sum) or excluding elements.

	# So, it is important to keep the state of the max_sum seen so far,
	# When determining if including or not a new element into the subarray,  will increase or decrease the max_sum.

	# Moreover, if including an element decrease the sum to that point to a value < 0
	# Then, that element (and elements before it) should not be included and discard the subset (to that point) completely, from the subarray.

	def max_sub_array_sum(self, nums):
		max_sum = 0
		curr_sum = 0
		for n in nums:
			curr_sum += n
			# If by including the element, the curr_sum so far becomes negative
			# Then, it is discarded (along with the elements ' the subset' up to this point), the sum is reset to 0, and the subarray restart
			if curr_sum < 0:
				curr_sum = 0
			else:
				# Otherwise, update the max_sum everytime curr_sum gets a new calculated value that is positive
				max_sum = max(max_sum, curr_sum)
		return max_sum


print(Solution().max_sub_array_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(Solution().max_sub_array_sum([-1, -4, 3, 8, 1]))  # 12
