"""
Fixed Point

Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i. Return -1 if no such i exists.

Example 1:
Input: [-10,-5,0,3,7]
Output: 3
Explanation:
For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.

Example 2:
Input: [0,2,5,8,17]
Output: 0
Explanation:
A[0] = 0, thus the output is 0.

Example 3:
Input: [-10,-5,3,4,7,9]
Output: -1
Explanation:
There is no such i that A[i] = i, thus the output is -1.
Note:

1 <= A.length < 10^4
-10^9 <= A[i] <= 10^9
"""


def find_fixed_point_helper(low, high, nums):
	if low == high:
		return None

	mid = int((low + high) / 2)  # (low + high) // 2
	if nums[mid] == mid:
		return mid
	if nums[mid] < mid:
		return find_fixed_point_helper(mid+1, high, nums)
	else:
		return find_fixed_point_helper(low, mid, nums)


def find_fixed_point_recur(nums):
	return find_fixed_point_helper(0, len(nums), nums)


def find_fixed_point_iter(nums):
	low = 0
	high = len(nums)

	while (low != high):
		mid = int((low + high) / 2)
		if nums[mid] == mid:
			return mid
		if nums[mid] < mid:
			low = mid + 1
		else:
			high = mid

	return None


print(find_fixed_point_recur([-5, 1, 3, 4]))  # 1
print(find_fixed_point_iter([-5, 1, 3, 4]))  # 1
print(find_fixed_point_recur([-5, -4, 0, 1, 4, 10, 25]))  # 4
print(find_fixed_point_iter([-5, -4, 0, 1, 4, 10, 25]))  # 4
