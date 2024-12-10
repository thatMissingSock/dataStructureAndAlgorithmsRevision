def duplicate(M, r, c):
    """The aim of this function is to take in a matrix(M) and two integers (r and c) and output a new matrix. The new
    matrix should be made of rm * rc instead of the normal m * c."""

    tempList = []
    tempMatrix = []
    columnCount = 0
    rowCount = 0

    while (rowCount < r):
        for row in range(len(M)):
            while (columnCount < c):
                for column in range(len(M[0])):
                    tempList.append(M[row][column])
                columnCount += 1
            tempMatrix.append(tempList)
            tempList = []
            columnCount = 0
        rowCount += 1
    rowCount = 0
    return  tempMatrix

# test code below
M = [[1, 2, 3], [4, 5, 6]]
N = duplicate(M, 1, 2)
print(f"{N} should be \n[[1, 2, 3, 1, 2, 3], [4, 5, 6, 4, 5, 6]]")
print("")

M = [[1, 2, 3], [4, 5, 6]]
N = duplicate(M, 2, 1)
print(f"{N} should be \n[[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]")
print("")

M = [[1, 2, 3], [4, 5, 6]]
N = duplicate(M, 2, 2)
print(f"{N} should be \n[[1, 2, 3, 1, 2, 3], [4, 5, 6, 4, 5, 6], [1, 2, 3, 1, 2, 3], [4, 5, 6, 4, 5, 6]]")
print("")

M = [[1, 2], [3, 4]]
N = duplicate(M, 3, 3)
print(f"{N} should be \n[[1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4], [1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4], [1, 2, 1, 2, 1, 2], [3, 4, 3, 4, 3, 4]]")
print("")

M = [[1, 2, 3], [4, 5, 6]]
N = duplicate(M, 1, 1)
print(f"{N} should be \n[[1, 2, 3], [4, 5, 6]]")
