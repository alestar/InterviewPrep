"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
*This problem is similar to the Sort list of 3 Unique Numbers*
"""

from collections import defaultdict


class Solution(object):
	def sort_colors_dict(self, colors):
		# Count the colors in a dict (hashmap)
		colors_dict = defaultdict(int)
		for c in colors:
			colors_dict[c] += 1

		index = 0
		# Rebuild the color [] by re-adding the elements sorted, for each color
		for i in range(colors_dict[0]):
			colors[index] = 0
			index += 1
		for i in range(colors_dict[1]):
			colors[index] = 1
			index += 1
		for i in range(colors_dict[2]):
			colors[index] = 2
			index += 1

	def sort_colors_pointers(self, colors):
		low_idx = 0
		high_index = len(colors) - 1
		curr_index = 0

		while curr_index <= high_index:
			if colors[curr_index] == 0:
				colors[low_idx], colors[curr_index] = colors[curr_index], colors[low_idx]
				low_idx += 1
				curr_index += 1
			elif colors[curr_index] == 2:
				colors[high_index], colors[curr_index] = colors[curr_index], colors[high_index]
				high_index -= 1
			else:
				curr_index += 1


colors_arr = [0, 2, 1, 0, 1, 1, 2]
Solution().sort_colors_dict(colors_arr)
print(colors_arr)
# [0, 0, 1, 1, 1, 2, 2]

colors_arr = [0, 2, 1, 0, 1, 1, 2]
Solution().sort_colors_pointers(colors_arr)
print(colors_arr)
# [0, 0, 1, 1, 1, 2, 2]
