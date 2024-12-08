def replace(M, a, b):
    """The aim of this function is to take in a matrix(M) and check each element to see if it matches the integer a.
    If it does match integer a then it should be replaced with integer b."""

    tempMatrix = []
    tempList = []

    for row in range(len(M)):
        for column in range(len(M[0])):
            if (M[row][column] == a):
                M[row][column] = b
            tempList.append(M[row][column])
        tempMatrix.append(tempList)
        tempList = []
    return (tempMatrix)

M = [   [1, 0], [0, 1]]
replace(M, 0, 2)
print(M)

M = [[1, 0, 1], [0, 1, 0]]
replace(M, 1, 2)
print(M)

M = [[1, 1], [1, 1]]
replace(M, 3, 4)
print(M)

M = [[1, 1, 1], [1, 1, 1]]
replace(M, 1, 3)
print(M)

M = [[1]]
replace(M, 1, 3)
print(M)