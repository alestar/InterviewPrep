"""

Validate if a given 2D array represents a valid Sudoku configuration.
grid1 = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]
Output: True
"""


def validateSudoku(m):

    #Valid is square not necessary


    n = len(m)
    #If is size 1 return True if value 1
    if (n==1 and m[0][0]!=1):
        return False

    for i in range(len(m)):
        observed = set()
        for j in range (len(m[0])):
            if m[i][j] in observed: # is a duplicate
                return False

            if m[i][j] > n or m[i][j] < 1 : # is invalid
                return False
            else:
                observed.add(m[i][j])
    # Sudoku is valid for all row orientation

    # Check for all col orientation
    for i in range(len(m)):
        observed = set()
        for j in range (len(m[0])):
            if m[j][i] in observed: # is a duplicate
                return False

            if m[j][i] > n or m[j][i] < 1 : # is invalid
                return False
            else:
                observed.add(m[j][i])

    return True

grid1 = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]

print(validateSudoku(grid1)) # True