def zero_mat(n):
    """this function takes in one argument (n) to make a new matrix that is dimensions of n * n with the elements all
    being 0, THERE SHOULD BE NO ALIASING"""
    tempMatrix = []
    rowCount = 0
    columnCount = 0
    for row in range(n):
        tempMatrix.append([])
        for column in range(n):
            tempMatrix[rowCount].append(0)
        rowCount += 1
    for matrix in range(len(tempMatrix)):
        print(tempMatrix[matrix])
    return(tempMatrix)

print(zero_mat(3))

# this is just to test if the code works and there truly is no aliasing
# newMatrix = zero_mat(6)
# newMatrix[0][1] = 2
#
# for i in range(len(newMatrix)):
#     print(newMatrix[i])