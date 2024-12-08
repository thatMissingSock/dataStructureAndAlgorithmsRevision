def transpose(M) :
    """So the aim of this function is to take in a matrix(M) and then transpose it outputting another matrix. By
    transpose, I mean swapping the values of m(rows) and n(columns)."""

    rowCount = 0
    columnCount = 0
    newRowsLength = len(M[0])
    newColumnsLength = len(M)
    tempWholeList = []
    tempMatrix = []
    tempList = []
    cCount = 0
    rCount = 0
    for row in range(len(M)):
        for column in range(len(M[0])):
            tempWholeList.append(M[row][column])

    while (rowCount < newRowsLength):
        while (columnCount < newColumnsLength):
            tempList.append(M[columnCount][rowCount])
            columnCount += 1
        rowCount += 1
        tempMatrix.append(tempList)
        tempList = []
        columnCount = 0
    return tempMatrix

# test cases

M = [[1, 1], [2, 2], [3, 3]]
print(transpose(M))

M = [[1, 2, 3], [1, 2, 3]]
print(transpose(M))

# Symmetric matrix
M = [[1, -2, 3], [-2, 4, -5], [3, -5, 6]]
print(transpose(M))

M = [[1, 2, 3, 4]]
print(transpose(M))

M = [[1], [2], [3], [4]]
print(transpose(M))

M = [[5]]
print(transpose(M))

