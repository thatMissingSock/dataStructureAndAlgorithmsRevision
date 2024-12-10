def row_cycle(M, r):
    """
    This is the same thing except that we DON'T return a new matrix but rather modify the EXISTING matrix.
    :param M: A matrix.
    :param r: A value of how many cycles.
    :return: A modified matrix.
    """

    tempMatrix = [None] * len(M)
    max = len(M) - 1
    for row in range(len(M)):
        newPlacement = r + row
        newPlacement %= (max + 1)
        tempMatrix[newPlacement] = M[row]

    for row in range(len(M)):
        M[row] = tempMatrix[row]

    return M

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THE BLOODY ORIGINAL "SHOULD BE" WERE WRONG~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# test code below
M = [[1, 1], [2, 2], [3, 3]]
row_cycle(M, 1)
print(M, "should now be", [[3, 3], [1, 1], [2, 2]])

M = [[1, 1], [2, 2], [3, 3]]
row_cycle(M, 2)
print(M, "should now be", [[2, 2], [3, 3], [1, 1]])

M = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
row_cycle(M, -1)
print(M, "should now be", [[2, 4, 6], [3, 6, 9], [1, 2, 3]])

M = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
row_cycle(M, 4)
print(M, "should now be", [[3, 6, 9], [1, 2, 3], [2, 4, 6]])

M = [[1, 2, 3]]
row_cycle(M, 7)
print(M, "should now be", [[1, 2, 3]])

M = [[1], [2], [3]]
row_cycle(M, -2)
print(M, "should now be", [[3], [1], [2]])