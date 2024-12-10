
def row_cycle(M, r):
    """
    The aim of this is to take in a matrix (M) and return a new matrix but with each value 'cycled' r amount of times.
    If r was 3 then everything moves down 3 rows and if r was -3 then everything moves up 3 rows.
    :param M: A matrix.
    :param r: A value representing how many times it should be cycled.
    :return: A new CYCLED matrix.
    """
    tempMatrix = [None] * len(M)
    max = len(M) - 1
    for row in range(len(M)):
        newPlacement = r + row
        newPlacement %= (max + 1)
        tempMatrix[newPlacement] = M[row]

    return tempMatrix

# ~~~~~~~~~~THE BLOODY ORIGINAL "SHOULD BE" WERE WRONG WHICH LEAD ME TO SPEND 45 MINS ON THIS DAMN QUESTION~~~~~~~~~~
# test code below
M = [[1, 1], [2, 2], [3, 3]]
N = row_cycle(M, 1)
print(N, "should be " , [[3, 3], [1, 1], [2, 2]])

M = [[1, 1], [2, 2], [3, 3]]
N = row_cycle(M, 2)
print(N, "should be", [[2, 2], [3, 3], [1, 1]])

M = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
N = row_cycle(M, -1)
print(N, "should be", [[2, 4, 6], [3, 6, 9], [1, 2, 3]])

M = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
N = row_cycle(M, 4)
print(N, "should be", [[3, 6, 9], [1, 2, 3], [2, 4, 6]])

M = [[1, 2, 3]]
N = row_cycle(M, 7)
print(N, "should be", [[1, 2, 3]])

M = [[1], [2], [3]]
N = row_cycle(M, -2)
print(N, "should be", [[3], [1], [2]])