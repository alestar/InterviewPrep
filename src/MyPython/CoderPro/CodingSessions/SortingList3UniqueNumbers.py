def sort_nums_using_dic(nums,  low, mid, high):
	num_counts = {}
	for n in nums:
		# Search for the number as a key
		# If it DOES NOT exist in the dict, return 0
		# If it DOES return the current count
		# Finally, increment curr count by one for that number
		num_counts[n] = num_counts.get(n, 0) + 1
	# To conclude
	# Build an array with all numbers count, in order
	return ([low] * num_counts.get(low, 0) +
			[mid] * num_counts.get(mid, 0) +
			[high] * num_counts.get(high, 0))


def sort_num_using_pointers(nums, low, mid, high):
	low_idx = 0
	high_idx = len(nums) - 1
	curr_idx = 0
	while curr_idx <= high_idx:

		# If it is a low number, it will be sorted to the start of the array
		# swap curr_idx value with low_idx
		# increase low_idx, since a low number was sorted to the beginning of the array
		# and increase the curr_idx to continue with next number
		if nums[curr_idx] == low:
			nums[curr_idx], nums[low_idx] = nums[low_idx], nums[curr_idx]
			low_idx += 1
			curr_idx += 1

		# If it is a middle number, there is nothing to sort, it stay were it is
		# and increase the curr_idx to continue with next number
		elif nums[curr_idx] == mid:
			curr_idx += 1

		# If it is a high number, it will be sorted to the end of the array
		# swap curr_idx value with high_idx and only decrease high_idx,
		# since a high number was sorted to the end of the array curr_idx wont be incremented,
		# because the number that just got swapped from the end to the front, has not being inspected yet
		elif nums[curr_idx] == high:
			nums[curr_idx], nums[high_idx] = nums[high_idx], nums[curr_idx]
			high_idx -= 1
	return nums


arr = [3, 3, 2, 1, 3, 2, 1]
print(sort_nums_using_dic(arr, 1, 2, 3))  # [1, 1, 2, 2, 3, 3, 3]
print(sort_num_using_pointers(arr, 1, 2, 3))  # [1, 1, 2, 2, 3, 3, 3]
