"""
Number of 1 bits

Given an integer, find numbers of 1 bits it has.

"""

def one_bits(n):
	count = 0
	while n > 0:
		# Perform an AND operation with the '1'
		# to verify is the value at that pos is '1'
		if n & 1:
			count = count + 1
			# >> is equivalent to div by 2, since is dividing by 2 everytime then O(log(n))
		# Shift to the right to check the next binary value
		n >>= 1
	return count


print(one_bits(23))  # 23 is represented as 0b10111
