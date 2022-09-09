"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
	[0 0 0 0 0 0 0
	0 0 0 0 0 0 0
	0 0 0 0 0 0 G]

Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


class Solution(object):
	def unique_paths_recur(self, m, n):
		if m == 1 or n == 1:
			return 1
		return self.unique_paths_recur(m - 1, n) + self.unique_paths_recur(m, n - 1)

	def unique_paths_DP(self, m, n):
		# Initialize cache with 0 unique paths for all the cells
		cache = [[0] * n] * m

		# Initialize first col to '1', since there is only one path going down
		for i in range(m):
			cache[i][0] = 1

		# Initialize first col to '1', since there is only one path going right
		for j in range(n):
			cache[0][j] = 1

		# Now, use dynamic programing to build the rest of the cell total unique path amounts
		# By adding the previous computed top cell
		# and the prev computed left cell
		for c in range(1, m):
			for r in range(1, n):
				cache[c][r] = cache[c][r-1] + cache[c-1][r]

		# Finally return the last cell/pos unique paths amount
		return cache[-1][-1]


print(Solution().unique_paths_recur(5, 3))
# 15

print(Solution().unique_paths_DP(5, 3))
# 15

print(Solution().unique_paths_DP(7, 3))
# 28
