"""

Multiply All except itself

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Example 1:
Input: nums = [1,2,3]
Output: [6,3,2]

Example 2:
Input: nums = [0,1,2,3]
Output: [6,0,0,0]

Example 3:
Input: nums = [0,1,0,3]
Output: [0,0,0,0]
"""


def multiply_except_self(arr):
	factor = 1
	zero_count = 0
	for num in arr:
		if num != 0:
			factor *= num
		else:
			zero_count += 1

	if zero_count >= 2:
		arr = [0] * len(arr)

	for i in range(len(arr)):
		if zero_count == 1:
			if arr[i] == 0:
				arr[i] = factor
			else:
				arr[i] = 0
		else:
			try:
				arr[i] = int(factor / arr[i])
			except:
				ZeroDivisionError

	return arr


print(multiply_except_self([1, 2, 3]))  # [6, 3 ,2]
print(multiply_except_self([0, 1, 2, 3]))  # [6, 0, 0, 0]
print(multiply_except_self([0, 1, 0, 2, 3]))  # [0, 0, 0, 0, 0]
