def rec_flatten(M):
    """
    Same restrictions as before. When given a matrix (M) the function should return a list containing all the elements
    starting from the first row and reading each column from left to right.
    :param M: A matrix.
    :return: A list containing all the elements of the matrix.
    """

    if M == []:
        return []

    head = M[0]
    tail = M[1:]

    return head + rec_flatten(tail)


# test code below as provided by GPT
# Test cases for rec_flatten(M)

# Base case: Empty matrix
M = []
print(f"{rec_flatten(M)} should be []")  # Expected output: []

# Single-row matrix
M = [[1, 2, 3]]
print(f"{rec_flatten(M)} should be [1, 2, 3]")  # Expected output: [1, 2, 3]

# Two-row matrix
M = [[1, 2], [3, 4]]
print(f"{rec_flatten(M)} should be [1, 2, 3, 4]")  # Expected output: [1, 2, 3, 4]

# Multi-row matrix with varying lengths
M = [[1, 2, 3], [4, 5], [6]]
print(f"{rec_flatten(M)} should be [1, 2, 3, 4, 5, 6]")  # Expected output: [1, 2, 3, 4, 5, 6]

# Matrix with empty rows
M = [[], [1, 2], [], [3, 4]]
print(f"{rec_flatten(M)} should be [1, 2, 3, 4]")  # Expected output: [1, 2, 3, 4]

# Single element matrix
M = [[42]]
print(f"{rec_flatten(M)} should be [42]")  # Expected output: [42]

# Matrix with negative numbers
M = [[-1, -2, -3], [-4, -5], [-6]]
print(f"{rec_flatten(M)} should be [-1, -2, -3, -4, -5, -6]")  # Expected output: [-1, -2, -3, -4, -5, -6]

# Matrix with mixed data types
M = [[1, "a"], [3.5, None], [True, 0]]
print(f"{rec_flatten(M)} should be [1, 'a', 3.5, None, True, 0]")  # Expected output: [1, 'a', 3.5, None, True, 0]

# Large matrix
M = [[i for i in range(5)] for _ in range(3)]  # 3 rows of [0, 1, 2, 3, 4]
print(f"{rec_flatten(M)} should be {list(range(5)) * 3}")  # Expected output: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

# Matrix with nested lists as elements (invalid structure for flattening)
M = [[1, [2, 3]], [4, [5, 6]]]
print(f"{rec_flatten(M)} should be [1, [2, 3], 4, [5, 6]]")  # Expected output: [1, [2, 3], 4, [5, 6]]
