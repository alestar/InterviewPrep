"""
INSTRUCTIONS: IMPLEMENT THIS METHOD.  Do not change the function signature or the tests won't run properly.

Given a list of positive integers and a non-negative number K, return which contiguous elements
of the list sum to K.  For example, if the list is [5, 2, 4, 3, 1] and K is 9,
then it should return [2, 4, 3], since 2 + 4 + 3 = 9.  Note [5, 4] is not a solution because
it is not a *contiguous* sub-array.

Note: Empty-list [] is viewed as having a sum of 0.

Note: If there is more than one such subarray, return the first from left.

Note: If the problem has no solution, return None.

To Consider:
[2, 2, 2, ..., 2, 1, 2, 2, 2, ..., 2], 999 = 998 + 1 = 997 + 2 = 996 + 3...
[5, 2, 4, 3, 1]

Example 1:
Input: [1, 2, 3, 4, 5], k: 9
Output:  [2, 3, 4]

Test 2
Input: [1, 2, 3, 4, 5], k: 16
Output:  None

Example 3:
Input: [1, 2, 3, 4, 5], k: 0
Output:  []

Example 4:
Input: [1, 5, 3, 3], k: 6
Output:  [1, 5]

Example 5:
Input: [9, 8, 7], k: 7
Output:  [7]

Example 6:
Input: [1, 1, 2, 3, 4, 5], k: 9
Output:  [2, 3, 4]

Example 7:
Input: [1, 5, 42], k: 47
Output:  [5, 42]



"""
from collections import deque


def sum_to_k_brute_force(nums, k):
	res = []

	for i in range(len(nums)):
		r = k - nums[i]
		if r < 0:
			continue
		res.append(nums[i])
		j = i + 1

		while r > 0 and j < len(nums):
			res.append(nums[j])
			r = r - nums[j]
			if r == 0:
				return res
			if r < 0:
				res = []
				break
			j += 1

		if r > 0:
			return None

	return res


def sum_to_k_queue(nums, k):
	s = 0
	queue = deque()
	queue.append(nums[0])
	s += nums[0]
	for i in range(1, len(nums)):
		if s < k:
			s = s + nums[i]
			queue.append(nums[i])
		if s > k:
			if queue:
				# Discard the start fo the sub-array
				# Since it makes the sum larger than target
				s -= queue.popleft()
		if s == k:
			return queue
	return None


def sum_to_k_pointers(nums, k):
	s = 0
	start = 0
	end = 1
	for i in range(len(nums)):
		if s < k:
			s = s + nums[i]
			end += 1
		if s > k:
			# Discard the start fo the sub-array
			# Since it makes the sum larger than target
			s = s - nums[start]
			start += 1
		if s == k:
			return nums[start:end-1]
	return None

# print(sum_to_k_brute_force([1, 2, 3, 4, 5], 9))  # [2, 3, 4]
# print(sum_to_k_brute_force([1, 2, 3, 4, 5], 16))  # None
# print(sum_to_k_brute_force([1, 2, 3, 4, 5], 0))  # []
# print(sum_to_k_brute_force([1, 5, 3, 3], 6))  # [1, 5]
# print(sum_to_k_brute_force([9, 8, 7], 7))  # [7]
# print(sum_to_k_brute_force([1, 1, 2, 3, 4, 5], 9))  # [2, 3, 4]
# print(sum_to_k_brute_force([1, 5, 42], 47))  # [5, 42]
#
# print(sum_to_k_queue([1, 2, 3, 4, 5], 9))  # [2, 3, 4]
# print(sum_to_k_queue([1, 2, 3, 4, 5], 16))  # None
# print(sum_to_k_queue([1, 2, 3, 4, 5], 0))  # []
# print(sum_to_k_queue([1, 5, 3, 3], 6))  # [1, 5]
# print(sum_to_k_queue([9, 8, 7], 7))  # [7]
# print(sum_to_k_queue([1, 1, 2, 3, 4, 5], 9))  # [2, 3, 4]
# print(sum_to_k_queue([1, 5, 42], 47))  # [5, 42]


print(sum_to_k_pointers([1, 2, 3, 4, 5], 9))  # [2, 3, 4]
print(sum_to_k_pointers([1, 2, 3, 4, 5], 16))  # None
print(sum_to_k_pointers([1, 2, 3, 4, 5], 0))  # []
print(sum_to_k_pointers([1, 5, 3, 3], 6))  # [1, 5]
print(sum_to_k_pointers([9, 8, 7], 7))  # [7]
print(sum_to_k_pointers([1, 1, 2, 3, 4, 5], 9))  # [2, 3, 4]
print(sum_to_k_pointers([1, 5, 42], 47))  # [5, 42]


