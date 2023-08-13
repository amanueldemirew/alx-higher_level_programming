def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    for i in range(row):
        col = len(matrix[i])
        for j in range(col):
            if (j == col - 1):
                print("{:d}".format(matrix[i][j]),end='')
            else:
                print("{:d}".format(matrix[i][j]),end=' ')
        print()
