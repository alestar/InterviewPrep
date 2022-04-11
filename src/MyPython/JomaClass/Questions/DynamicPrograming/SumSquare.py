"""
Sum of Squares

Given a number n, find the least number of squares needed to sum up to the num

Example :
Input: 13
Output: 2

squares[1, 4, 9]

1 -> 1 [1]
2 -> 1 + 1 [1]
3 -> 1 + 1 + 1 [1]
4 -> 1 [1]
5 -> 4 + 1 [2]
6 -> 4 + 1 + 1 [3]
7 -> 4 + 1 + 1 + 1 [4]
8 -> 4 + 4 [2]
9 -> 1 [1]
10 -> 9 + 1 [2]
11 -> 9 + 1 + 1 [3]
12 -> 4 + 4 + 4 [3] < 9 + 1 + 1 + 1[4]
13 -> 9 + 4 + 4 [2]


Time Complexity O(n * srt(n))

"""


def min_square_sums_counts(num):
	squares = []

	# Generate squares that are smaller than the num
	i = 1
	while i * i <= num:
		squares.append(i * i)
		i = i + 1
	# print(squares)

	# Initialize the array with the max count for the target num + 1
	# because there are 'nums' way of using 1 to form the target num
	# and since it's looking for the min
	# and because 0 is included
	min_addends_count_to_create_num_arr = [num] * (num + 1)

	# Base Case: There are no numbers needed to create 0, hence value is 0
	min_addends_count_to_create_num_arr[0] = 0

	# Determine how many ways are to sum up to num value
	for i in range(num + 1):

		# Using the squares that are less than the num
		for s in squares:

			# Represents the num to be created/added up to by selecting/using/adding one of the squares num
			num_to_create = i + s

			# Check for out of bounce
			if num_to_create < len(min_addends_count_to_create_num_arr):

				# Determine ways to create a number (i + s) by using:
				# - existing/curr num of ways to create number (i + s) -> calculated from prev iterations
				# - new ways to create number (i + s), from num of prev ways at [i] and adding/selecting one of the choices (i.e 1, 4 or 9)
				addends_count_to_create_num_at_target = min_addends_count_to_create_num_arr[num_to_create]
				addends_count_to_create_num_from_idx = min_addends_count_to_create_num_arr[i] + 1
				min_addends_count = min(addends_count_to_create_num_at_target, addends_count_to_create_num_from_idx)
			min_addends_count_to_create_num_arr[num_to_create] = min_addends_count
		# print(min_addends_count_to_create_num_arr)

	# Return the last to obtain the min_addends_count of the param num
	return min_addends_count_to_create_num_arr[-1]


print("For num: '3' -> " + str(min_square_sums_counts(3)))  # 3
print("For num: '4' -> " + str(min_square_sums_counts(4)))  # 1
print("For num: '9' -> " + str(min_square_sums_counts(9)))  # 1
print("For num: '13' -> " + str(min_square_sums_counts(13)))  # 2
