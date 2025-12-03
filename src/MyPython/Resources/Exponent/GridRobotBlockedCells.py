"""
Given a factory represented as a 2D grid with some cells blocked and some containing robots, determine if the robots can collectively reach all unblocked cells.
Robots can move in four directions (up, down, left, right) and cannot pass through blocked cells.
"""
from collections import deque
def can_robots_reach_all_cells(factory_grid):
    rows = len(factory_grid)
    cols = len(factory_grid[0]) if rows > 0 else 0

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    total_unblocked = 0
    robot_positions = []

    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Count unblocked cells and find robot positions
    for r in range(rows):
        for c in range(cols):
            if factory_grid[r][c] != 'B':  # Not blocked
                total_unblocked += 1
                if factory_grid[r][c] == 'R':  # Robot found
                    robot_positions.append((r, c))

    # BFS to explore reachable cells from all robots
    queue = deque(robot_positions)
    for r, c in robot_positions:# Mark robot starting positions as 'visited'
        visited[r][c] = True

    reachable_count = len(robot_positions) # Start with the number of robots

    # Perform BFS. How? by exploring all four directions from each cell in the queue.Queue starts with all robot positions.
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions: # Explore all four directions where 'dr' and 'dc' are the changes in row and column indices respectively. Example: up (-1,0), down (1,0), left (0,-1), right (0,1)
            nr, nc = r + dr, c + dc # Calculate new row and column indices. Example
            if 0 <= nr < rows and 0 <= nc < cols:
                if factory_grid[nr][nc] != 'B' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    reachable_count += 1
                    queue.append((nr, nc))

    return reachable_count == total_unblocked

# Example usage:
factory1 = [
    ['R', 'W', 'W', 'B'],
    ['W', 'B', 'W', 'W'],
    ['W', 'W', 'R', 'W'],
    ['B', 'W', 'W', 'W']
]
print(can_robots_reach_all_cells(factory1))  # Output: True
factory2 = [
    ['R', 'B', 'W', 'B'],
    ['B', 'B', 'W', 'W'],
    ['W', 'W', 'R', 'W'],
    ['B', 'W', 'W', 'W']
]
print(can_robots_reach_all_cells(factory2))  # Output: True. Why? because some W cells are blocked off by B cells for both robots
factory3 = [
    ['R', 'W', 'W', 'W'],
    ['W', 'B', 'B', 'W'],
    ['W', 'W', 'R', 'W'],
    ['W', 'W', 'W', 'W']
]
print(can_robots_reach_all_cells(factory3))  # Output: True
factory4 = [
    ['R', 'B', 'W', 'W'],
    ['B', 'B', 'W', 'W'],
    ['W', 'W', 'B', 'B'],
    ['W', 'W', 'B', 'R']
]
print(can_robots_reach_all_cells(factory4))  # Output: False
factory5 = [
    ['R', 'W', 'W', 'W'],
    ['B', 'B', 'B', 'B'],
    ['W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'R']
]
print(can_robots_reach_all_cells(factory5))  # Output: False
factory6 = [
    ['R', 'W', 'B', 'W'],
    ['W', 'W', 'B', 'W'],
    ['W', 'W', 'B', 'W'],
    ['W', 'W', 'B', 'R']
]
print(can_robots_reach_all_cells(factory6))  # Output: True
factory7 = [
    ['R', 'W', 'W', 'W'],
    ['W', 'B', 'W', 'W'],
    ['W', 'W', 'B', 'W'],
    ['W', 'W', 'W', 'R']
]
print(can_robots_reach_all_cells(factory7))  # Output: True
factory8 = [
    ['R', 'B', 'B', 'W'],
    ['B', 'B', 'B', 'W'],
    ['W', 'W', 'B', 'W'],
    ['W', 'W', 'B', 'R']
]
print(can_robots_reach_all_cells(factory8))  # Output: False