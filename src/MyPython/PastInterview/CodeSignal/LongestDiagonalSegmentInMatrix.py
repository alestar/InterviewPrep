"""
Given a matrix of integers, with each element containing either 0, 1, or 2,
your task is to find the longest diagonal segment which matches the following pattern:
    1, 2, 0, 2, 0, 2, 0, ... (where the first element is 1, and then 2 and 0 are repeating infinitely), and finishes at a matrix border.
Return the length of this diagonal segment. The diagonal segment:
May start at any matrix element May go toward any possible diagonal direction Must end at an element in the first or last row or column S
See the example videos below. Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(matrix.length2 · matrix[0].length2) will fit within the execution time limit.
Example For matrix = [[0, 0, 1, 2], [0, 2, 2, 2], [2, 1, 0, 1]] the output should be solution(matrix) = 3.
"""
def solution(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    max_length = 0
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # 4 diagonal directions

    def expected(length):
        if length == 0:
            return 1
        elif length % 2 == 1:
            return 2
        else:
            return 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 1:  # must start with 1
                continue
            for dr, dc in directions:
                x, y = r, c
                length = 0
                last_x, last_y = r, c

                while 0 <= x < rows and 0 <= y < cols:
                    if matrix[x][y] != expected(length):
                        break
                    length += 1
                    last_x, last_y = x, y
                    x += dr
                    y += dc

                # Only count if last valid cell is at a border
                if last_x == 0 or last_x == rows-1 or last_y == 0 or last_y == cols-1:
                    max_length = max(max_length, length)

    return max_length




# Example usage:
matrix = [[0, 0, 1, 2],
          [0, 2, 2, 2],
          [2, 1, 0, 1]]
print(solution(matrix))  # Output: 3
matrix1 = [[1, 2, 0, 2, 0],
           [2, 0, 2, 0, 2],
           [0, 2, 1, 2, 0],
           [2, 0, 2, 0, 2],
           [0, 2, 0, 2, 0]]
print(solution(matrix1))  # Output: 1
matrix2 = [[1, 2, 0, 2, 0, 2],
           [2, 0, 2, 0, 2, 0],
           [0, 2, 1, 2, 0, 2],
           [2, 0, 2, 0, 2, 0],
           [0, 2, 0, 2, 0, 2],
           [2, 0, 2, 0, 2, 1]]
print(solution(matrix2))  # Output: 1
matrix3 = [[1, 0, 0, 0, 0],
            [0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0]]
print(solution(matrix3))  # Output: 5

