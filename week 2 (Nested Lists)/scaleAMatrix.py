def scale(M, c):
    """So the aim of this function is to take in a matrix(M) and an integer(c). The new outputted matrix should be
    the EXACT SAME LENGTH AND WIDTH as the original but the elements inside should be multiplied by intgeer c."""
    tempList = []
    tempMatrix = []
    for row in range(len(M)):
        for column in range(len(M[0])):
            tempNum = 0
            tempNum = M[row][column] * c
            tempList.append(tempNum)
        tempMatrix.append(tempList)
        tempList = []
    return tempMatrix

# test cases
M = [[1, 2], [3, 4]]
print(scale(M, 2))

M = [[1, -2], [-3, 4]]
print(scale(M, -1))

M = [[1, -2], [-3, 4]]
print(scale(M, 0))

M = [[5]]
print(scale(M, 3))