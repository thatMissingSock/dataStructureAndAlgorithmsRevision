def big_discrep(M, N):
    """So the aim of this function is to take in two matrices(M and N) and find out the biggest discrepancy in them.
    For example if in matrix M[0][0] was 3 yet in matrix N[0][0] the value is 1 then the discrepancy is (-)2 (we ONLY
    care about absolute calues and thus any negative integers are ignored for this function. We then need to output
    in a list what the discrepancy value is and what the coordinates of the discrepancy lies. You can output it as
    the following [num, [a, b]]."""
    tempDiscrepancy = 0
    tempCoordinates = []
    for row in range(len(M)):
        for column in range(len(M[0])):
            tempM = M[row][column]
            tempN = N[row][column]
            newDiscrepancy = abs(tempM - tempN)
            if tempDiscrepancy == 0:
                tempDiscrepancy = newDiscrepancy
                tempCoordinates = [row, column]
            elif(tempDiscrepancy < newDiscrepancy):
                tempDiscrepancy = newDiscrepancy
                tempCoordinates = [row, column]
    tempOutput = [tempDiscrepancy, tempCoordinates]
    return tempOutput

# testing the function
M = [[1, 2, 3], [3, 2, 1]]
N = [[2, 4, 6], [9, 6, 3]]
print(big_discrep(M, N))


M = [[1, 2, 3, 4, 5, 6]]
N = [[-1, -2, -3, -4, -5, -6]]
print(big_discrep(M, N))

M = [[1, 2], [3, 4], [5, 6]]
N = [[-1, -2], [-3, -4], [-5, -6]]
print(big_discrep(M, N))

M = [[5]]
N = [[12]]
print(big_discrep(M, N))