"""
Magical Candy Bags
You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?
Signature
int maxCandies(int[] arr, int K)
Input
1 ≤ N ≤ 10,000
1 ≤ k ≤ 10,000
1 ≤ arr[i] ≤ 1,000,000,000
Output
A single integer, the maximum number of candies you can eat in k minutes.
Example 1
N = 5
k = 3
arr = [2, 1, 7, 4, 2]
output = 14
In the first minute you can eat 7 pieces of candy. That bag will refill with floor(7/2) = 3 pieces.
In the second minute you can eat 4 pieces of candy from another bag. That bag will refill with floor(4/2) = 2 pieces.
In the third minute you can eat the 3 pieces of candy that have appeared in the first bag that you ate.
In total you can eat 7 + 4 + 3 = 14 pieces of candy.


"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
import heapq


def max_candies(arr, k):
	# Write your code here
	arr = [i * -1 for i in arr]
	output = []
	heapq.heapify(arr)
	for _ in range(k):
		output.append(heapq.heappop(arr))
		heapq.heappush(arr, int(output[-1] / 2))
	return -1 * sum(output)


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.


def printInteger(n):
	print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
	global test_case_number
	result = False
	if expected == output:
		result = True
	right_tick = '\u2713'
	wrong_tick = '\u2717'
	if result:
		print(right_tick, 'Test #', test_case_number, sep='')
	else:
		print(wrong_tick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printInteger(expected)
		print(' Your output: ', end='')
		printInteger(output)
		print()
	test_case_number += 1


if __name__ == "__main__":
	n_1, k_1 = 5, 3
	arr_1 = [2, 1, 7, 4, 2]
	expected_1 = 14
	output_1 = max_candies(arr_1, k_1)
	check(expected_1, output_1)

	n_2, k_2 = 9, 3
	arr_2 = [19, 78, 76, 72, 48, 8, 24, 74, 29]
	expected_2 = 228
	output_2 = max_candies(arr_2, k_2)
	check(expected_2, output_2)

	# Add your own test cases here
