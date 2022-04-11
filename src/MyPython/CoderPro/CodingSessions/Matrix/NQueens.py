"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9

"""


def n_queens_helper(n, row, col, asc_diag, desc_diag, queen_pos_assigned):
	# When a position has been assigned for all the queens
	# Then, the board is completed and the list of assigned pos for the n queens is returned
	if len(queen_pos_assigned) == n:
		return queen_pos_assigned

	# Otherwise, traverse the remaining rows from the last queen pos assignation
	# Starting from the next row available
	# Which is at the length of how many pos are assigned so far,
	# Like so :
	# 	0 pos assigned, curr_row = 0
	# 	1 pos assigned, curr_row = 1
	# 	2 pos assigned, curr_row = 2
	# 	etc.
	curr_row = len(queen_pos_assigned)

	# Traverse each col of the curr_row (n queens -> n col)
	for curr_col in range(n):

		# Check if all attack directions for the current queen pos are open/available (no other queen attacking)
		# To verify if the new pos can be assigned to the curr queen
		if col[curr_col] and row[curr_row] and asc_diag[curr_row + curr_col] and desc_diag[curr_row - curr_col]:

			# If all attack directions for the current queen pos are open/available
			# Update the corresponding attack directions for the curr queen pos assignation to 'False' (no other queens can use this pos)
			col[curr_col] = False
			row[curr_row] = False
			asc_diag[curr_row + curr_col] = False
			desc_diag[curr_row - curr_col] = False

			# Add new pos assigned (curr_row, curr_col) to the list of positions for all the queens
			queen_pos_assigned.append((curr_row, curr_col))

			# Call recur with board updated (all the attacked directions of the board updated with the last queen pos assignation)
			n_queens_helper(n, row, col, asc_diag, desc_diag, queen_pos_assigned)

			# Verify if solution has been reach after recursive call
			# To determine if backtrack is necessary or not
			if len(queen_pos_assigned) == n:
				return queen_pos_assigned

			# Otherwise, it means that not all  the queens could be assigned to a pos in the board
			# Therefore, backtrack and try again with different pos, from the current assignation state
			# Reset all the attacked directions to true to make it available again, for next pos reassignment
			col[curr_col] = True
			row[curr_row] = True
			asc_diag[curr_row + curr_col] = True
			desc_diag[curr_row - curr_col] = True

			# Finally, remove the assignation of the curr post from the result list
			# Since, it was not a valid assignation
			queen_pos_assigned.pop()

	return queen_pos_assigned


def n_queens(n):
	# Given the board is size n x n, initially the board is a available for any pos and any attack direction

	# Available for all the cols
	col = [True] * n

	# Available for all the row
	row = [True] * n

	# Available for all the ascending diagonals
	asc_diag = [True] * (n * 2 - 1)

	# Available for all the descending diagonals
	desc_diag = [True] * (n * 2 - 1)

	return n_queens_helper(n, col, row, asc_diag, desc_diag, [])


print(n_queens(5))
# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]