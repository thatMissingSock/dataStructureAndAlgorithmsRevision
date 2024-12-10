def make_symm(M):
    """
    This takes in a matrix (M) and returns a symmetrical matrix.
    [[0, 1, 1],      ============    [[0, 1, 1].
     [0, 0, 1],      should equal    [1, 0, 1],
     [0, 0, 0]]      ============    [1, 1, 0]]
    :param M: A matrix.
    :return: A NEW symmetrical matrix.
    """
    tempMatrix = [None] * len(M)
    for row in range(len(M)):
        tempMatrix[row] = M[row]

    for row in range(len(tempMatrix)):
        for column in range(len(tempMatrix[0])):
            if tempMatrix[row][column] != tempMatrix[column][row]:
                if tempMatrix[row][column] == 1:
                    tempMatrix[column][row] = tempMatrix[row][column]
                else:
                    tempMatrix[row][column] = tempMatrix[column][row]

    return tempMatrix

# test code below
# M already symmetric

M = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
print(f"{make_symm(M)} should be \n[[1, 0, 0], [0, 0, 0], [0, 0, 0]]")
print("")

M = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(f"{make_symm(M)} should be \n[[0, 0, 0], [0, 1, 0], [0, 0, 0]]")
print("")

M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(f"{make_symm(M)} should be \n[[1, 0, 0], [0, 1, 0], [0, 0, 1]]")
print("")

# M not symmetric

M = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
print(f"{make_symm(M)} should be \n[[0, 0, 1], [0, 0, 0], [1, 0, 0]]")
print("")

M = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
print(f"{make_symm(M)} should be \n[[0, 0, 1], [0, 0, 0], [1, 0, 0]]")
print("")

M = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
print(f"{make_symm(M)} should be \n[[0, 1, 0], [1, 0, 0], [0, 0, 0]]")
print("")

M = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
print(f"{make_symm(M)} should be \n[[0, 1, 0], [1, 0, 0], [0, 0, 0]]")
print("")

M = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]
print(f"{make_symm(M)} should be \n[[0, 0, 0], [0, 0, 1], [0, 1, 0]]")
print("")

M = [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
print(f"{make_symm(M)} should be \n[[0, 0, 0], [0, 0, 1], [0, 1, 0]]")
print("")

M = [[0, 1, 1], [0, 0, 0], [0, 0, 0]]
print(f"{make_symm(M)} should be \n[[0, 1, 1], [1, 0, 0], [1, 0, 0]]")
print("")

M = [[0, 1, 1],
     [0, 0, 1],
     [0, 0, 0]]
print(f"{make_symm(M)} should be \n[[0, 1, 1], [1, 0, 1], [1, 1, 0]]")


