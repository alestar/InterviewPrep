"""
Running Median

Given a stream of numbers. Compute the median for each new element.

Example:
	Input:  [2, 1, 4, 5, 3, 0, 5]
	Output: [2, 1.5, 2, 3.0, 2, 2, 2]

The median is the middle value in an ordered integer list. If the size is odd then the median is in the middle and is calculated: pos1 = (n + 1)/2
However, if the size of the list is even, there is no middle value and the median is the mean of the two middle values: pos2= n/2 => (pos1 + pos2)/2

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5

[2, 1, 4, 7, 2, 0, 5]
max_heap  <= median <= min_heap

Looking at '7':
	2    2    4  -> median = 2 + 4/2 = 3.0
    \        /
     1      7
Looking at '2':
  	2   3.0   2  -> median = 2 (return min of right side because it has more elements)
    \        / \
     1      7   4

Looking at '0':
    2    2    2  -> median = 2 +2 /2 = 2
   / \       / \
  0   1     7   4

Looking at '5':
    2    2    2  -> median = 2 (return min of right side because it has one more elements)
   / \       / \
  0   1     5   4
		   /
		  7

"""
import heapq


def running_median(stream):
	min_heap = []
	max_heap = []
	medians = []
	# iterate throw all the number is the stream
	for num in stream:
		# Add each number to the corresponding heap
		add(num, min_heap, max_heap)
		# Rebalance when size is not equilibrated
		rebalance(min_heap, max_heap)
		# Add the curr obtained median to the medians list
		medians.append(obtain_median(min_heap, max_heap))
	return medians


def add(num, min_heap, max_heap):
	# If there are no elements (or just 1) in the heaps
	# Then, push the num value into the max_heap ('left half', with 'smaller' elements than the curr median)
	if len(min_heap) + len(max_heap) <= 1:
		heapq.heappush(max_heap, -num)
		return

	# If there is more than one element
	# Then, calculate the current median
	median = obtain_median(min_heap, max_heap)

	# If the num is 'bigger' than the curr median
	# Then, push the num value into the min_heap ('right half', with 'bigger' elements than the curr median)
	if num > median:
		heapq.heappush(min_heap, num)

	# If the num is 'smaller' than the curr median
	# Then, push the num value into the max_heap ('left half', with 'smaller' elements than the curr median)
	else:
		# Since 'heapq' is a min_heap by definition, in order to make it behave as a max_heap, the values must be inserted as negative,
		# because then the biggest number with (-) sing becomes the smallest, and therefore will be put at the top of the min_heap (now behaving as a "max_heap"),
		# as it would have been the case on a real max_heap
		heapq.heappush(max_heap, -num)


def rebalance(min_heap, max_heap):
	# If there more than 1 elements in either heap
	# then, pop it from the greater one and push it into the lesser
	if len(min_heap) > len(max_heap) + 1:
		root = heapq.heappop(min_heap)
		heapq.heappush(max_heap, -root)
	elif len(min_heap) < len(max_heap) + 1:
		root = heapq.heappop(max_heap)
		heapq.heappush(max_heap, root)


def obtain_median(min_heap, max_heap):
	# If there more elements on the min_heap (right half with elements that are bigger than the curr median)
	# Then the amount of element is 'odd', and the new median is = the 'min value' of the 'right half', with 'bigger' elements than the curr median
	if len(min_heap) > len(max_heap):
		return min_heap[0]
	# If there more elements on the max_heap ('left half' with elements that are smaller than the curr median)
	# Then the amount is still 'odd', and the new median is = the 'max value' of the 'left half', with 'smaller' elements than the curr median
	elif len(min_heap) < len(max_heap):
		# since max_heap is storing the elements with a (-) sing, another (-) sing will be use to convert it to a positive number
		return -max_heap[0]
	# If the amount of elements in both half (left and right) is equal or even
	# then, the median is the average of :
	# 	the 'min value' of the 'right half', with 'bigger' elements than the curr median, and
	# 	the 'max value' of the 'left half', with 'smaller' elements than the curr median
	else:
		# mIf the amount is even return the average of top values of each heap
		return (min_heap[0] + -max_heap[0]) / 2.0


stream1 = [2, 1, 4, 7, 2, 0, 5]
stream2 = [2, 1, 4, 5, 3, 0, 5]
print("Running media of stream1: " + str(stream1))
print(running_median(stream1))  # [2, 2, 2, 3.0, 3, 3, 3]
print("Running media of stream2: " + str(stream2))
print(running_median(stream2))  # [2, 2, 2, 3.0, 3, 3, 3]

