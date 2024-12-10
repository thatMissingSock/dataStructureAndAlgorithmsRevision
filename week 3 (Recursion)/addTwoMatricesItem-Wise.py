def rec_addlists(x, y):
    """
    Same restrictions as before. This function takes in two lists (x and y) and should return a new list that contains the
    combined elements of both. The length of the new list should be the same as the lengths of either x or y.
    :param x: A list.
    :param y: A list.
    :return: A new list containing all of the elements in x and y.
    """
    if x == []:
        return []
    if y == []:
        return []


    headOfX = x[0]
    tailOfX = x[1:]
    headOfY = y[0]
    tailOfY = y[1:]

    forcedRecursion = rec_addlists(tailOfX, tailOfY)

    return [headOfX + headOfY] + forcedRecursion

def rec_addmats(M, N):
    """
    Same restrictions as before. We are doing the same as the code above, but instead of combining the elements in a list we
    are combining the elements in two different matrices (M and N). The row length and column length of the new matrix should
    be equal to that of N or M (we assume N and M are the same length too!).
    :param M: A matrix.
    :param N: A matrix.
    :return: A new combined matrix.
    """
    if M == []:
        return []
    if N == []:
        return []

    headOfM = M[0]
    headOfN = N[0]
    tailOfM = M[1:]
    tailOfN = N[1:]

    forcedMatrixRecursion = rec_addmats(tailOfM, tailOfN)
    tempSummedRow = rec_addlists(headOfM, headOfN)
    return [tempSummedRow] + forcedMatrixRecursion

# test code provided by GPT

# Test cases for rec_addmats(M, N)

# Base case: Two single-row matrices
M, N = [[1, 2, 3]], [[4, 5, 6]]
print(f"{rec_addmats(M, N)} should be [[5, 7, 9]]")  # Expected output: [[5, 7, 9]]

# Two-row matrices
M, N = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
print(f"{rec_addmats(M, N)} should be [[6, 8], [10, 12]]")  # Expected output: [[6, 8], [10, 12]]

# Multi-row matrices with varying row lengths
M, N = [[1, 2, 3], [4, 5], [6]], [[7, 8, 9], [10, 11], [12]]
print(f"{rec_addmats(M, N)} should be [[8, 10, 12], [14, 16], [18]]")  # Expected output: [[8, 10, 12], [14, 16], [18]]

# Matrices with negative numbers
M, N = [[-1, -2, -3], [-4, -5]], [[-6, -7, -8], [-9, -10]]
print(f"{rec_addmats(M, N)} should be [[-7, -9, -11], [-13, -15]]")  # Expected output: [[-7, -9, -11], [-13, -15]]

# Matrices with zeros
M, N = [[0, 0, 0], [0, 0]], [[0, 0, 0], [0, 0]]
print(f"{rec_addmats(M, N)} should be [[0, 0, 0], [0, 0]]")  # Expected output: [[0, 0, 0], [0, 0]]

# Matrices with floating-point numbers
M, N = [[1.5, 2.5], [3.5, 4.5]], [[0.5, 1.5], [2.5, 3.5]]
print(f"{rec_addmats(M, N)} should be [[2.0, 4.0], [6.0, 8.0]]")  # Expected output: [[2.0, 4.0], [6.0, 8.0]]

# Large matrices
M = [[i for i in range(5)] for _ in range(3)]  # 3 rows of [0, 1, 2, 3, 4]
N = [[i for i in range(5, 10)] for _ in range(3)]  # 3 rows of [5, 6, 7, 8, 9]
expected = [[i + j for i, j in zip(row1, row2)] for row1, row2 in zip(M, N)]
print(f"{rec_addmats(M, N)} should be {expected}")  # Expected output: Element-wise sum of M and N

# Uneven row lengths
M, N = [[1, 2], [3]], [[4, 5], [6]]
print(f"{rec_addmats(M, N)} should be [[5, 7], [9]]")  # Expected output: [[5, 7], [9]]

