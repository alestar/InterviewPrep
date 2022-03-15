maze_board_1 = [[".", ".", ".", "."],
                [".", "x", "x", "x"],
                [".", ".", ".", "x"],
                ["x", "x", ".", "."]]

maze_board_2 = [[".", ".", ".", "."],
                ["x", "x", "x", "x"],
                [".", ".", ".", "x"],
                ["x", "x", ".", "."]]


def print_maze(maze):
    for row in maze:
        row_print = ""
        for value in row:
            row_print += value + " "
        print(row_print)


# Joma Class Solution
def solve_maze(maze):
    if len(maze) < 1 or len(maze[0]) < 1:
        return None
    return solve_maze_helper(maze, [], 0, 0)


def solve_maze_helper(maze, sol, pos_row, pos_col):
    # Get size of maze
    num_row = len(maze)
    num_col = len(maze[0])

    # Base Cases:
    # Case 1: Robot is already Home (final coordinates of maze)
    if pos_row == num_row - 1 and pos_col == num_col - 1:
        return sol

    # Case 2: Robot is out of Bound
    if pos_row >= num_row or pos_col >= num_col:
        return None

    # Case 3: Robot is on an obstacle
    if maze[pos_row][pos_col] == "x":
        return None

    # Recursive Cases:
    # Try moving right
    sol.append("r")
    sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col + 1)
    if sol_going_right is not None:
        return sol_going_right

    # Moving 'Right' didn't work -> backtrack and try to go down
    sol.pop()

    # Try moving 'Down'
    sol.append("d")
    sol_going_down = solve_maze_helper(maze, sol, pos_row + 1, pos_col)
    if sol_going_down is not None:
        return sol_going_down

    # Moving 'Down' didn't work either -> No solution, Impossible to Backtrack
    sol.pop()

    return None


# More general Solution
def solve_maze_comprehensive(maze, start_row, start_col, goal_row, goal_col):
    if len(maze) < 1 or len(maze[0]) < 1:
        return None
    return solve_maze_helper_with_goal(maze, [], start_row, start_col, goal_row, goal_col)


def solve_maze_helper_with_goal(maze, sol, pos_row, pos_col, goal_row, goal_col):
    # Get size of maze
    num_row = len(maze)
    num_col = len(maze[0])

    # Base Cases:
    # Case 1: Robot is already Home (final coordinates of maze)
    if pos_row == goal_row and pos_col == goal_col:
        return sol

    # Case 2: Robot is out of Bound
    if pos_row >= num_row - 1 or pos_col >= num_col - 1:
        return None

    # Case 3: Robot is on an obstacle
    if maze[pos_row][pos_col] == "x":
        return None

    # Recursive Cases:
    # Try moving right
    sol.append("r")
    sol_going_right = solve_maze_helper_with_goal(maze, sol, pos_row, pos_col + 1, goal_row, goal_col)
    if sol_going_right is not None:
        return sol_going_right

    # Moving 'Right' didn't work -> backtrack and try to go down
    sol.pop()

    # Try moving 'Down'
    sol.append("d")
    sol_going_down = solve_maze_helper_with_goal(maze, sol, pos_row + 1, pos_col, goal_row, goal_col)
    if sol_going_down is not None:
        return sol_going_down

    # Moving 'Down' didn't work either -> No solution, Impossible to Backtrack
    sol.pop()

    return None

print_maze(maze_board_1)
print(solve_maze(maze_board_1))
print(solve_maze(maze_board_2))
print(solve_maze_comprehensive(maze_board_2, 2, 0, len(maze_board_2) - 1, len(maze_board_2[0]) - 1))
print(solve_maze_comprehensive(maze_board_2, 0, 0, 0, len(maze_board_2[0]) - 1))
