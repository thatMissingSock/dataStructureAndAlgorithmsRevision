def add(M, N):
    """The function should take in two matrices (M and N) and output a SINGLE MATRIX where all the corresponding
    elements in the same coordinates are summed up."""
    tempList = []
    tempMatrix = []

    for row in range(len(M)):
        for column in range(len(M[0])):
            tempNumM = M[row][column]
            tempNumN = N[row][column]
            tempSummedNum = tempNumM + tempNumN
            tempList.append(tempSummedNum)
        tempMatrix.append(tempList)
        tempList = []
    return tempMatrix

# test cases
M = [[0, 2], [3, 0]]
N = [[1, 0], [0, 4]]
R = add(M, N)
print(R)

R = add(M, M)
print(R)

M = [[1, 2], [3, 4], [5, 6]]
N = [[-1, 1], [1, -1], [-1, 1]]
R = add(M, N)
print(R)

M = [[0, 1, 2]]
N = [[2, 1, 0]]
R = add(M, N)
print(R)

M = [[3]]
N = [[2]]
R = add(M, N)
print(R)