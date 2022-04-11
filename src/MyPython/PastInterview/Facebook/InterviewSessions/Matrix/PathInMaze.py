# You are given a game board represented as a 2D array of zeroes and ones. Zero stands for passable positions and one stands for impassable positions. Design an algorithm to find a path from top left corner to bottom right corner.
# For example, for the following board:
# entrance -> 0 0 0 0 0 0 0
#             0 0 1 0 0 1 0
#             0 0 1 0 1 1 0
#             0 0 1 0 1 0 1
#             1 1 1 0 0 0 0 -> exit
# a possible path is:
# entrance -> + + + + 0 0 0
#             0 0 1 + 0 1 0
#             0 0 1 + 1 1 0
#             0 0 1 + 1 0 1
#             1 1 1 + + + + -> exit
# Assuming a zero-indexed grid of rows and columns, we'd return:
# (0, 0) -> (0, 1) -> (0, 2) -> (0, 3) -> (1, 3) -> (2, 3) ->
#   (3, 3) -> (4, 3) -> (4, 4) -> (4, 5) -> (4, 6)

class Solution:
	def __init__(self):
		self.path = [(0, 0)]

	# def __repr__(self):
	# 	return f"{str(item) + '->' for item in path}"

	def maz_solve(self, m):
		visited = set()
		return self._maze_solve_helper(m, 0, 0, self.path, visited)

	def _maze_solve_helper(self, m, row, col, path, visited):

		# Add the curr pos to visited set to avoid revisiting same nodes/cells
		if (row, col) in visited:
			return None
		else:
			visited.add((row, col))

		# Check if current pos is out of bound -> backtracking
		if row >= len(m) or row < 0 or col >= len(m[0]) or col < 0:
			return None

		# Base case check that row and col are at the end
		if row == len(m) - 1 and col == len(m[0]) - 1:
			return path

		# Check if the pos is invalid -> backtracking
		if m[row][col] == 1:
			return None

		# Proceed to continue moving in the maze
		# Attempt moving Up
		# If there is a solution path from moving in that direction returned
		# Otherwise Backtrack
		path.append((row - 1, col))
		sol_moving_up = self._maze_solve_helper(m, row - 1, col, path, visited)
		if sol_moving_up is not None:
			return path
		else:
			path.pop()

		# Attempt moving Down
		# If there is a solution path from moving in that direction returned
		# Otherwise Backtrack
		path.append((row + 1, col))
		sol_moving_down = self._maze_solve_helper(m, row + 1, col, path, visited)
		if sol_moving_down is not None:
			return path
		else:
			path.pop()

		# Attempt moving Right
		# If there is a solution path from moving in that direction returned
		# Otherwise Backtrack
		path.append((row, col + 1))
		sol_moving_right = self._maze_solve_helper(m, row, col + 1, path, visited)
		if sol_moving_right is not None:
			return path
		else:
			path.pop()

		# Attempt moving Left
		# If there is a solution path from moving in that direction returned
		# Otherwise Backtrack
		path.append((row, col - 1))
		sol_moving_left = self._maze_solve_helper(m, row, col - 1, path, visited)
		if sol_moving_left is not None:
			return path
		else:
			path.pop()

		# If at the end no solution path has been found recursively
		# Then return None
		return None


maze = [[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 1, 0],
		[0, 0, 1, 0, 1, 0, 1],
		[1, 1, 1, 0, 0, 0, 0]]
sol = Solution()
print(*sol.maz_solve(maze), sep=' -> ')
# print(sol.path)
