def big_discrep(M, N):
    """
    The aim of this is to take in two matrices of the SAME DIMENSIONS and return a list in this format:
    [the value of the biggest discrepancy [the index of said discrepancy]]. If one matrix value is 4 and the other is -3
    then the discrepancy is 7 (as that is the abs value between these two).
    :param M: A matrix.
    :param N: A matrix.
    :return: A list containing the discrepancy and where it is located.
    """
    biggestDiscrepancy = abs(M[0][0] - N[0][0])
    tempCoordinates = [0, 0]

    for row in range(len(M)):
        for column in range(len(M[0])):
            tempDiscrepancy = abs(M[row][column] - N[row][column])
            if tempDiscrepancy > biggestDiscrepancy:
                biggestDiscrepancy = tempDiscrepancy
                tempCoordinates[0] = row
                tempCoordinates[1] = column

    output = [biggestDiscrepancy, tempCoordinates]
    return output
# test code below
M = [[1, 2, 3], [3, 2, 1]]
N = [[2, 4, 6], [9, 6, 3]]
print(big_discrep(M, N), "should be", [6, [1, 0]])

M = [[1, 2, 3, 4, 5, 6]]
N = [[-1, -2, -3, -4, -5, -6]]
print(big_discrep(M, N), "should be", [12, [0, 5]])

M = [[1, 2], [3, 4], [5, 6]]
N = [[-1, -2], [-3, -4], [-5, -6]]
print(big_discrep(M, N), "should be", [12, [2, 1]])

M = [[5]]
N = [[12]]
print(big_discrep(M, N), "should be", [7, [0, 0]])