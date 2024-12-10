def ind_nonzero_row(M):
    """basically, this should take in a matrix and should output lists of the values which is not 0. Take [1,2,0,5,0,
    2] for example, it should return [0,1,3,5] skipping 2 and 4 since they are 0 integers."""
    tempRow = len(M)
    tempColumn = len(M[0])
    columnCount = 0
    rowCount = 0
    tempAnswer = []

    for i in range(tempRow):
        tempAnswer.append([])

    for row in range(tempRow):
        for column in range(tempColumn):
            if (M[rowCount][columnCount] != 0):
                tempAnswer[rowCount].append(columnCount)
            columnCount += 1
        columnCount = 0
        rowCount += 1
    return tempAnswer

# test code below
M = [[0, 0, 5], [0, 7, 0]]
print(ind_nonzero_row(M), "should be", [[2], [1]])

M = [[0, 5, 6], [7, 8, 0]]
print(ind_nonzero_row(M), "should be", [[1, 2], [0, 1]])

M = [[0, 0, 3], [0, 3, 0], [3, 0, 0]]
print(ind_nonzero_row(M), "should be", [[2], [1], [0]])

M = [[0, 0, 0], [3, 2, 1], [0, 0, 0]]
print(ind_nonzero_row(M), "should be", [[], [0, 1, 2], []])

M = [[0]]
print(ind_nonzero_row(M), "should be", [[]])

M = [[9]]
print(ind_nonzero_row(M), "should be", [[0]])