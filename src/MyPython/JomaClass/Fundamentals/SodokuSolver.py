board_1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]


# Use to pretty print board
def print_board(board):
    for row in board:
        row_print = ""
        for value in row:
            row_print += str(value) + " "
        print(row_print)


# Use to pretty print board
def print_board_fancy(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("-------------------------")
        row_print = ""
        for j in range(len(board[0])):
            if j % 3 == 0:
                row_print += "| "
            if board[i][j] == 0:
                row_print += "  "
            else:
                row_print += str(board[i][j]) + " "
        print(row_print + "|")
    print("-------------------------")


# Use to fnd first empty cell
def find_zero_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return [i, j]
    return []


# Determines if value can be assigned or if is already in use on the board
def is_valid(board, row, col, value, block_size):
    # Iterates throw the entire row (move horizontally)
    for i in range(len(board)):
        if board[row][i] == value:
            return False

    # Iterates throw the entire col (move vertically)
    for i in range(len(board[row])):
        if board[i][col] == value:
            return False

    # Determine starting coordinates of the current block to iterates throw it.
    start_row = (row // block_size) * block_size  # Floor division will give '0', '1' or '2' etc
    start_col = (col // block_size) * block_size  # Multiplied by 'block_size' will give:
    # The starting cell pos of the block

    # Iterate throw the current block
    for i in range(start_row, start_row + 3):  # iterates throw rows of the block
        for j in range(start_col, start_col + 3):  # iterates throw cols of the block
            if board[i][j] == value:
                return False
    return True


def sudoku_solver_helper(board, block_size=3):
    #  Base Case : Attempt to find an empty/zero cell
    zero_cell = find_zero_cell(board)
    if not zero_cell:  # If there aren't any cell left with value 0
        return board  # Then, the 'Sudoku' is complete, because there are no more 0 num to replace

    # Recursive Case : Attempt replace that zero cell with a value
    else:
        # and see if there is a 'Sudoku' solution for the new value
        zero_cell_row, zero_cell_col = zero_cell[0], zero_cell[1]
        print("looking at zero_cell: [" + str(zero_cell_row) + ", " + str(zero_cell_col) + "]")

        for val in range(1, 10):
            if is_valid(board, zero_cell_row, zero_cell_col, val, block_size):
                board[zero_cell_row][zero_cell_col] = val
                sol = sudoku_solver_helper(board, block_size)

                #  Check if the new solution is valid
                if not sol:  # If there is no solution then backtrack
                    board[zero_cell_row][zero_cell_col] = 0  # by resetting the cell to 0 and trying with the next num
                else:
                    return sol
    return None


def sudoku_solver(board):
    return sudoku_solver_helper(board)


#  --------------------------------------- Aux Method testing ---------------------------------------

# print_board(board_1)
print_board_fancy(board_1)
# print(find_first_zero_val_pos(board_1))
# print(is_valid(board_1, 0, 2, 1))
# print(is_valid(board_1, 0, 7, 9))
# print(is_valid(board_1, 0, 2, 8))
# print(is_valid(board_1, 0, 2, 7))
# print(is_valid(board_1, 0, 3, 5))

#  --------------------------------------- Main Method testing ---------------------------------------
print_board(sudoku_solver(board_1))
