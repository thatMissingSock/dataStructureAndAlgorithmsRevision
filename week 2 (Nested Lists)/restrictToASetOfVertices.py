def restrict(M, vs):
    """
    The question says that we should take in a matrix (M) and get rid of ALL indices found in the list (vs). Except that
    the "ideal" answers show that the only things that should remain are the vertices found inside the list???
    :param M: A matrix.
    :param vs: A list of indices.
    :return: Another matrix ONLY CONTAINING THE INDICES IN VS (IM FOLLOWING THE IDEAL ANSWERS).
    """
    tempMatrix = [None] * len(M)
    for row in range(len(tempMatrix)):
        tempMatrix[row] = [None] * len(M[0])
    for row in range(len(M)):
        for column in range(len(M[0])):
            tempMatrix[row][column] = M[row][column]

    totalIndices = []
    for i in range(len(M)):
        if i not in vs:
            totalIndices.append(i)

    for delRow in range(len(totalIndices)):
        count = 0
        count += totalIndices[delRow]
        while count > (len(tempMatrix) - 1):
            count -= 1
        del tempMatrix[count]

    for delColumn in range(len(totalIndices)):
        for row in range(len(tempMatrix)):
            count = 0
            count += totalIndices[delColumn]
            while count > (len(tempMatrix[row]) - 1):
                count -= 1

            del tempMatrix[row][count]

    return tempMatrix




# test code below
M = [[1, 2, 3], [4, None, 6], [7, 8, 9]]
print(restrict(M, [0, 1]), "should be", [[1, 2], [4, None]])

print(restrict(M, [1, 2]), "should be", [[None, 6], [8, 9]])

print(restrict(M, [0, 2]), "should be", [[1, 3], [7, 9]])

print(restrict(M, [0, 1, 2]), "should be", [[1, 2, 3], [4, None, 6], [7, 8, 9]])

print(restrict(M, [1]), "should be", [[None]])