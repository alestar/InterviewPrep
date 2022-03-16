"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109

"""

from functools import cmp_to_key


def largest_num(nums):
	sorted_nums = sorted(nums, key=cmp_to_key(
		lambda a, b:
		1 if str(a) + str(b) < str(b) + str(a)
		else -1)
		)
	return ''.join(str(n) for n in sorted_nums)


def largest_num_compare(nums):
	def compare (a, b):
		if str(a) + str(b) < str(b) + str(a):
			return 1
		else:
			return -1

	str_nums = [str(n) for n in sorted(nums, key = cmp_to_key(compare))]
	return ''.join(str_nums)


print(largest_num([17, 7, 2, 45, 72]))
print(largest_num_compare([17, 7, 2, 45, 72]))
# 77245217