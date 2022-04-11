"""
Revenue Milestones
We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones.
Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.

Signature
int[] getMilestoneDays(int[] revenues, int[] milestones)
Input
revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.
Output
Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.
Example
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
Explanation
On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that FB has >= $200 of total revenue.
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getMilestoneDays(revenues, milestones):
	# Write your code here
	N = len(revenues)
	cumulative_revenues = revenues[:]
	for i in range(1, N):
		cumulative_revenues[i] += cumulative_revenues[i-1]

	print(cumulative_revenues)

	def search(arr, target):
		lo, hi = 0, len(arr)
		while lo < hi:
			mid = lo + hi >> 1
			if arr[mid] >= target:
				hi = mid
			else:
				lo = mid + 1
		return lo

	res = []
	for m in milestones:
		idx = search(cumulative_revenues, m)
		res.append(idx + 1 if idx != N else -1)
	print(res)
	return res


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.


def printIntegerList(array):
	size = len(array)
	print('[', end='')
	for i in range(size):
		if i != 0:
			print(', ', end='')
		print(array[i], end='')
	print(']', end='')


test_case_number = 1


def check(expected, output):
	global test_case_number
	expected_size = len(expected)
	output_size = len(output)
	result = True
	if expected_size != output_size:
		result = False
	for i in range(min(expected_size, output_size)):
		result &= (output[i] == expected[i])
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printIntegerList(expected)
		print(' Your output: ', end='')
		printIntegerList(output)
		print()
	test_case_number += 1


if __name__ == "__main__":
	revenues_1 = [100, 200, 300, 400, 500]
	milestones_1 = [300, 800, 1000, 1400]
	expected_1 = [2, 4, 4, 5]
	output_1 = getMilestoneDays(revenues_1, milestones_1)
	check(expected_1, output_1)

	revenues_2 = [700, 800, 600, 400, 600, 700]
	milestones_2 = [3100, 2200, 800, 2100, 1000]
	expected_2 = [5, 4, 2, 3, 2]
	output_2 = getMilestoneDays(revenues_2, milestones_2)
	check(expected_2, output_2)

	revenues_3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
	milestones_3 = [100, 200, 500]
	expected_3 = [4, 6, 10]
	output_3 = getMilestoneDays(revenues_3, milestones_3)
	check(expected_3, output_3)
	# Add your own test cases here
