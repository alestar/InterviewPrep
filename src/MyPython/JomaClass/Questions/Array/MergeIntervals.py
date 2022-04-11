"""

Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def merge_intervals(intervals):
	res = []

	# Sorting by start of the interval guarantees that
	# the next interval is always going to start after the prev one
	for start, end in sorted(intervals, key=lambda x: x[0]):


		# If the 'curr start' is less than the prev interval's 'end'
		# Then, there is overlap
		# So the prev interval should be updated by consuming the overlap
		# (with prev start and the MAX between the two the ends of each interval)
		if res and start <= res[-1][1]:
			prev_start, prev_end = res[-1]
			# Merge
			res[-1] = (prev_start, max(prev_end, end))
		else:
			res.append((start, end))
	return res


print(merge_intervals(([1, 3], [5, 8], [4, 10], [20, 25])))
