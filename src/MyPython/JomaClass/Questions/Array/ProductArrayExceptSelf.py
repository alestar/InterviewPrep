"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
Solve without using division
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up:
Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


class Solution:
	# For this approach the <right side> products of the exclude item at index 'i' is computed first
	# Then, the <left side> products of the the excluded item 'i' ,
	# by multiplying the current left products with the already computed right product.
	# And storage the result in the exclude item index 'i'.
	def product_except_self(self, nums):
		res = [1] * len(nums)
		prod = 1

		# Calculate the accumulated products to the right side
		# And storage the prods in the result array
		for i in range(len(nums) - 2, -1, -1):
			prod *= nums[i+1]
			res[i] = prod

		print(res)

		# Calculate the total res products
		# by calculating the accumulated products to left
		# and multiplying the current calculated left products, with the already computed right product.
		prod = 1
		for i in range(1, len(nums)):
			prod *= nums[i-1]
			res[i] *= prod

		print(res)
		return res


print(Solution().product_except_self([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(Solution().product_except_self([2, 4, 1, 5, 3]))  # [60, 30, 120, 24, 40]
print(Solution().product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]

