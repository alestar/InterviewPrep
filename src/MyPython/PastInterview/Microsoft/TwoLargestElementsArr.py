"""
Find Two largest elements in a given array

Given an array of integers, write an algorithm to find the first two largest elements in the array.

Example:
a = [6, 8, 1, 9, 2, 1, 10]
Output: 10,9

a = [6, 8, 1, 9, 2, 1, 10, 10]
Output: 10,10

a = [6]
Output: Invalid Input, array size is less than 2

Approach:
Take two variables; let’s call them first and second and mark them as -∞.
Iterate through the array and for each element (let’s call it current),
Compare it with the first and if first is less, assign the first value to second and assign current to first.
If above step is not true then current element might be a candidate of second highest element, so check if current>second,if yes then assign it to second.
"""


def two_biggest(arr):

	if not arr or len(arr) < 2:
		return None

	largest_2 = -1
	largest_1 = -1

	for i in range(len(arr)):
		if arr[i] > largest_1:
			largest_2 = largest_1
			largest_1 = arr[i]
		elif arr[i] > largest_2:
			largest_2 = arr[i]
	if largest_2 == largest_1 or largest_2 == -1 or largest_1 == -1:
		return None

	return largest_2, largest_1


print(two_biggest([6, 5, 10, 2]))
print(two_biggest([6, 5, 10, 2, 8, 4, 3, 7, 9, 11]))
