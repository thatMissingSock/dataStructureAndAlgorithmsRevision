def make_symm(M):
    """
    So this is essentially the same thing but instead of 0's and 1's we deal with weighted edges and None's. WE ONLY CARE
    IF IT HAS A VALUE OR NOT. WE DO NOT CARE IF THE VALUES ARE DIFFERENT.
    :param M: A weighted matrix.
    :return: A symmetrical weighted matrix.
    """
    tempMatrix = [None] * len(M)
    for row in range(len(M)):
        tempMatrix[row] = M[row]

    for row in range(len(tempMatrix)):
        for column in range(len(tempMatrix)):
            if tempMatrix[row][column] is not None and tempMatrix[column][row] is None:
                tempMatrix[column][row] = tempMatrix[row][column]
            elif tempMatrix[row][column] is None and tempMatrix[column][row] is not None:
                tempMatrix[row][column] = tempMatrix[column][row]
    return tempMatrix

# test code below
M = [[1, -1], [None, 2]]
print(f"{make_symm(M)} should be \n[[1, -1], [-1, 2]]")
print("")

M = [[1, None], [None, 2]]
print(f"{make_symm(M)} should be \n[[1, None], [None, 2]]")
print("")

M = [[1, None, 3], [2, None, 6], [3, None, 9]]
print(f"{make_symm(M)} should be \n[[1, 2, 3], [2, None, 6], [3, 6, 9]]")
print("")

M = [[1, None, 3], [2, None, 6], [3, None, 9]]
print(f"{make_symm(M)} should be \n[[1, 2, 3], [2, None, 6], [3, 6, 9]]")
print("")

M = [[1]]
print(f"{make_symm(M)} should be \n[[1]]")
print("")

M = [[None, None], [None, 4]]
print(f"{make_symm(M)} should be \n[[None, None], [None, 4]]")
print("")