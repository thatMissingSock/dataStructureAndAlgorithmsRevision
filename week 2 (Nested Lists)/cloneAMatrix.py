def clone_mat(M):
    """So basically this takes in a matrix already and then expects a copy of the matrix without any aliasing"""
    tempRow = len(M)
    tempColumn = len(M[0])
    rowCount = 0
    columnCount = 0
    tempMatrix = []

    for row in range(tempRow):
        tempMatrix.append([])
        for column in range(tempColumn):
            tempMatrix[rowCount].append(M[row][column])
            columnCount += 1
        rowCount += 1
    return tempMatrix

toBeCloned = [[1,2,3], [4,5,6], [7,8,9]]
print(toBeCloned)
clonedMatrix = clone_mat(toBeCloned)
print(clonedMatrix)

# the following is to ensure there is no aliasing going on
# clonedMatrix[1][1] = 50
# print(toBeCloned)
# print(clonedMatrix)
