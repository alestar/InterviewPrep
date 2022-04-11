class Solution(object):
	def single_number_dic(self, nums):
		occurrence = {}

		for n in nums:
			occurrence[n] = occurrence.get(n, 0) + 1

		for key, value in occurrence.items():
			if value == 1:
				return key

	def single_number_xor(self, nums):
		unique = 0
		unique_xor = []
		for n in nums:
			unique ^= n
			unique_xor.append(unique)
		print(unique_xor)
		return unique


print(Solution().single_number_dic([4, 3, 2, 4, 1, 3, 2]))
print(Solution().single_number_xor([4, 3, 2, 4, 1, 3, 2]))
print(Solution().single_number_xor([2, 2, 2, 2, 1, 2, 2]))
print(Solution().single_number_xor([2, 2, 2, 2, 2, 2, 1]))
print(Solution().single_number_xor([0, 0, 0, 0, 1, 0, 0]))
print(Solution().single_number_xor([0, 0, 0, 0, 1, 1, 0]))
print(Solution().single_number_xor([0, 0, 0, 1, 1, 1, 0]))
print(Solution().single_number_xor([2, 2, 2, 2, 2, 2, 2]))
print(Solution().single_number_xor([2, 2, 2, 2, 2, 2]))
