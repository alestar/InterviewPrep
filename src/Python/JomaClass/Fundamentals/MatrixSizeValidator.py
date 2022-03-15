def print_matrix(m):
    if m == []:
        print("Empty Matrix")
        return

    num_rows = len(m)
    num_cols = len(m[0])
    for row in m:
        line_to_print = ""
        for num in row:
            line_to_print  += str(num) + ", "
        print(line_to_print)


def create_matrix(num_row, num_col):
    m = []
    for i in range(num_row):
        row = []
        for j in range(num_col):
            row.append(0)
        m.append(row)
    return m


def is_valid_matrix(m):
    if not m:
        return False
    num_row = len(m)
    num_col_for_all_row = len(m[0])
    for i in range(num_row):
        num_col = len(m[i])
        if num_col != num_col_for_all_row:  # num of col has to be equal for all row(s), to be a valid matrix
            return False
    return True


#
# print(is_valid_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(is_valid_matrix([[1, 2, 3], [4, 5], [7, 8, 9]]))


def matrix_multiply(a, b):  # m is the first matrix and n is the second

    if not is_valid_matrix(a) or not is_valid_matrix(b):  # Both must be valid matrix
        return None

    num_row_a = len(a)  # num_row of matrix A (m)
    num_col_a = len(a[0])  # num_col of matrix A (n)
    num_row_b = len(b)  # num_row of matrix B (k)
    num_col_b = len(b[0])  # num_col of matrix B (p)

    if num_col_a != num_row_b:  # the num_col in the 1st matrix must be equal to the num_row in the 2nd matrix n == k
        return None

    # The result matrix, known as the matrix product:
    pm = create_matrix(num_row_a, num_col_b)  # has the num_row of the 1st matrix and the num_col of the 2nd matrix
    print_matrix(pm)

    for i in range(num_row_a):
        for j in range(num_col_b):
            for k in range(num_row_b): # Iterate through num_col_a (n) or num_row_b (k)
                pm[i][j] += a[i][k] * b[k][j]

    return pm


matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[1, 2],
           [3, 4],
           [5, 6]]

print(matrix_multiply(matrix1, matrix2))
