def is_identity_matrix(matrix):
    i, j, c, d = 0, 0, 0, 0
    while (i < len(matrix)):
        while (j < len(matrix)):
            if ((i == j and matrix[i][j] == 1)):
                c = c + 1
            elif (i != j and matrix[i][j] == 0):
                d = d + 1

            j = j + 1
        i=i+1
        j=0
    print (c, d)


# Test Cases:

matrix1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
print(is_identity_matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]))