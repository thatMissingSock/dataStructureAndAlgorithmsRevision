def col_min_max(M):
    """The aim of this is to take in a matrix(M) and output pairs of the highest and lowest in another matrix. BUT
    the pairs should be based on the highest and lowest in the column. I.e. highest pair in [0,0], [1,0], [2,0], [3,
    0]"""
    tempMatrix = []
    tempList = []

    for column in range(len(M[0])):
        tempHighest = M[0][column]
        tempLowest = M[0][column]
        for row in range(len(M)):
            if (tempHighest < M[row][column]):
                tempHighest = M[row][column]
            if (tempLowest > M[row][column]):
                tempLowest = M[row][column]
        tempList.append(tempLowest)
        tempList.append(tempHighest)
        tempMatrix.append(tempList)
        tempList = []
    return (tempMatrix)

# test code below
M = [[6, 5, 4], [3, 4, 5], [3, 2, 1]]
print(col_min_max(M), "should be", [[3, 6], [2, 5], [1, 4]])

M = [[6], [5], [4]]
print(col_min_max(M), "should be", [[4, 6]])

M = [[6, 5, 4]]
print(col_min_max(M), "should be", [[6, 6], [5, 5], [4, 4]])

M = [[1, 2, 3], [-4, -5, -6]]
print(col_min_max(M), "should be", [[-4, 1], [-5, 2], [-6, 3]])

M = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
print(col_min_max(M), "should be", [[1, 3], [1, 3], [1, 3], [1, 3]])

M = [[9]]
print(col_min_max(M), "should be", [[9, 9]])