"""
1020. Number of Enclaves Difficulty: Medium

Hint
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

This script calculates the number of enclaves in a given grid.
An enclave is a region that is fully surrounded by land (denoted by '1') and is not connected to the boundary of the grid.

# Complexity Analysis
Time Complexity: O(m * n), where m is the number of rows and n is the
Space Complexity: O(m * n) in the worst case due to the recursion stack in DFS. number of columns in the grid. We may need to visit all cells in the grid.

"""
def num_enclaves(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return
        grid[r][c] = 0  # Mark the cell as visited by setting it to 0
        # Explore all four directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Start DFS from the boundary cells
    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 1:
                dfs(r, c)

    # Count the remaining land cells (enclaves)
    enclave_count = sum(grid[r][c] == 1 for r in range(rows) for c in range(cols))
    return enclave_count

def num_enclaves_2 (grid):
    if not grid or not grid[0]:
        return 0

    ROWS,COLS = len(grid), len(grid[0])
    visit = set()

    #Return num of land cell
    def dfs(r,c):
        if(r < 0 or r > ROWS
            or c < 0 or c > COLS
            or not grid[r][c] # cell is equal '0'
            or (r,c) in visit): # already visited
                return 0
        visit.add((r,c))
        res=1
        direct = [[0,1],[0,-1],[1,0],[-1,0]]
        for dr,dc in direct:
            dfs(r + dr, c+ dc)
        return res

    land, borderLand = 0, 0
    for r in range(ROWS):
        for c in range(COLS):
            land += grid[r][c]
            if (grid[r][c] and # cell is equal '1'
                (r,c) not in visit and # Not yet visited
                (c in [0, COLS-1] or r in [0, ROWS-1])): # In the border
                    borderLand+=dfs(r,c)

    return  land- borderLand

def print_grid(grid):
    print("Grid: ")
    for row in grid:
        print(row)
    print()


# Example 1:
grid1 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print_grid(grid1)
print("sol: ")
print(num_enclaves(grid1))  # Output: 3
print(num_enclaves_2(grid1))  # Output: 3

# Example 2:
grid2 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print_grid(grid2)
print("sol: ")
print(num_enclaves(grid2))  # Output: 0
print(num_enclaves_2(grid2))  # Output: 0

# Example 3:
grid3 = [[1,1,1,1,0,0],[1,0,0,1,0,0],[1,0,1,1,1,0],[0,0,0,0,0,0]]
print_grid(grid3)
print("sol: ")
print(num_enclaves(grid3))  # Output: 1
print(num_enclaves_2(grid3))  # Output: 1

#Example 4:
grid4 = [[0,0,0,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]
print_grid(grid4)
print("sol: ")
print(num_enclaves(grid4))  # Output: 8
print(num_enclaves_2(grid4))  # Output: 8
