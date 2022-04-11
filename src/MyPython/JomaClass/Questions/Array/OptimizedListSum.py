"""
Optimized List Sum

Create a class that initializes with a list of numbers and has one method called sum.

sum() should only take two parameters, start and end and return the sum of the list from start (inclusive) to end (exclusive).

"""


class ListFastSum(object):
	def __init__(self, nums):
		# Start at '0' so start and end correspond to the actual position in the array
		self.sum_up_to = []

		curr_sum = 0
		for num in nums:
			curr_sum += num
			self.sum_up_to.append(curr_sum)
		print(self.sum_up_to)  # [1, 3, 6, 10, 15, 21, 28]

		# Append a '0' at the end so when start_idx = 0 - 1 will point to the last element of the array (in reverse) and give value '0'
		# This way the index 0 of the array can be use for start_idx
		self.sum_up_to.append(0)
		print(self.sum_up_to)  # [0, 1, 3, 6, 10, 15, 21, 28,0]

	def sum(self, start_idx, end_idx):
		return self.sum_up_to[end_idx - 1] - self.sum_up_to[start_idx - 1]  # 15 - 3 = 12


class ListFastSum2(object):
	def __init__(self, nums):
		self.pre = [0]

		curr_sum = 0
		for num in nums:
			curr_sum += num
			self.pre.append(curr_sum)
		print(self.pre)

	def sum(self, start, end):
		return self.pre[end] - self.pre[start]


print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))  # 12 because 3 + 4 + 5 = 12
print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(0, 5))  # 15 because 1 + 2 + 3 + 4 + 5 = 15
print(ListFastSum2([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))  # 12 because 3 + 4 + 5 = 12
print(ListFastSum2([1, 2, 3, 4, 5, 6, 7]).sum(0, 5))  # 15 because 1 + 2 + 3 + 4 + 5 = 15
