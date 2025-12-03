"""
Imagine that you're exploring a mysterious labyrinth in the shape of a rectangular matrix, which contains obstacles and teleports. Starting from the upper-left corner, your goal is to reach the lower-right corner by first moving to the right, and then moving down if that doesn't work.

You are given integers n and m representing the dimensions of the labyrinth. You are also given obstacles and teleports, which are lists of the cells that contain all the obstacles and teleports, respectively.

Details about the labyrinth:

An obstacle cannot be traversed - if there's an obstacle in the cell to your right, try moving down. If there are obstacles in the cells to the right and below, stop immediately.
A teleport is a pair of cells (start, end). If you reach the start cell, you immediately move to the end cell..
Note that this doesn't work backwards: you cannot teleport from the end cell to the start cell.
It is guaranteed that all teleports have unique start cells (i.e. each cell in the labyrinth has one teleport at most).
It is guaranteed that the end cell for a teleport cannot be a start cell for another teleport.
It is also guaranteed that both the start and end cells of a teleport do not contain obstacles.
Any cell that doesn't contain an obstacle or a teleport is considered a free cell, and you can walk through it normally.
You start at the upper-left corner cell with coordinates (0, 0), and the goal is to reach the exit located at the cell with coordinates (n - 1, m - 1). You move according to the following rules:
First, you will always try moving to the right: if you're currently on the cell with coordinates (row, col), you will try moving to the cell with coordinates (row, col + 1).

If the destination cell (row, col + 1) is the starting point of a teleport, proceed to the coordinates of the end cell.
If the destination cell (row, col + 1) either contains an obstacle or is outside the bounds of the labyrinth, try moving down to the cell (row + 1, col).
If the destination cell (row + 1, col) is the starting point of a teleport, proceed to coordinates of the end cell.
If the destination cell (row + 1, col) either contains an obstacle or is outside the bounds of the labyrinth, stop moving and stay where you are.
Your task is to check whether you can reach the goal (exit of the labyrinth) by following the algorithm above, and to return the total number of cells you travelled through to reach the exit. Note that you should count all cells travelled, including the starting cell (0, 0), and both the start and end cells of all teleports. If it is not possible to reach the exit, return -1 if it's because of an obstacle or due to trying to go outside the bounds of the labyrinth, or -2 if it's because of teleportation (i.e., an infinite teleport loop).

It's guaranteed that the starting cell (0, 0) and the goal cell (n - 1, m - 1) do not contain an obstacle, or be the starting point of a teleport.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(n · m · (obstacles.length + teleports.length) will fit within the execution time limit.


"""
def solution(n, m, obstacles, teleports):
    obstacle_set = set((r, c) for r, c in obstacles)
    teleport_dict = { (sr, sc): (er, ec) for sr, sc, er, ec in teleports }

    row, col = 0, 0
    visited_teleports = set()
    steps = 1  # Starting cell counts as a step

    while (row, col) != (n - 1, m - 1):
        # Try to move right
        next_col = col + 1
        if (row, next_col) in teleport_dict:
            if (row, next_col) in visited_teleports:
                return -2  # Infinite teleport loop
            visited_teleports.add((row, next_col))
            row, col = teleport_dict[(row, next_col)]
            steps += 1  # Count teleport start cell
            steps += 1  # Count teleport end cell
        elif (row, next_col) in obstacle_set or next_col >= m:
            # Try to move down
            next_row = row + 1
            if (next_row, col) in teleport_dict:
                if (next_row, col) in visited_teleports:
                    return -2  # Infinite teleport loop
                visited_teleports.add((next_row, col))
                row, col = teleport_dict[(next_row, col)]
                steps += 1  # Count teleport start cell
                steps += 1  # Count teleport end cell
            elif (next_row, col) in obstacle_set or next_row >= n:
                return -1  # Blocked by obstacle or out of bounds
            else:
                row = next_row
                steps += 1
        else:
            col = next_col
            steps += 1

    return steps
# Example usage:
n = 4
m = 4
obstacles = [(0, 2), (1, 1), (2, 3)]
teleports = [(0, 1, 2, 0), (2, 1, 3, 2)]
print(solution(n, m, obstacles, teleports))  # Output: 6

n = 2
m = 4
obstacles = [[0,2]]
teleports = [[1,2,0,3]]

print(solution(n, m, obstacles, teleports))
