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

# test code provided by GPT
# Test cases for rec_addlists(x, y)

# Base case: Two empty lists
x, y = [], []
print(f"{rec_addlists(x, y)} should be []")  # Expected output: []

# Single-element lists
x, y = [5], [3]
print(f"{rec_addlists(x, y)} should be [8]")  # Expected output: [8]

# Two-element lists
x, y = [1, 2], [3, 4]
print(f"{rec_addlists(x, y)} should be [4, 6]")  # Expected output: [4, 6]

# Multi-element lists
x, y = [1, 2, 3], [4, 5, 6]
print(f"{rec_addlists(x, y)} should be [5, 7, 9]")  # Expected output: [5, 7, 9]

# Lists with negative numbers
x, y = [-1, -2, -3], [-4, -5, -6]
print(f"{rec_addlists(x, y)} should be [-5, -7, -9]")  # Expected output: [-5, -7, -9]

# Lists with a mix of positive and negative numbers
x, y = [1, -2, 3], [-1, 2, -3]
print(f"{rec_addlists(x, y)} should be [0, 0, 0]")  # Expected output: [0, 0, 0]

# Lists with zeros
x, y = [0, 0, 0], [0, 0, 0]
print(f"{rec_addlists(x, y)} should be [0, 0, 0]")  # Expected output: [0, 0, 0]


# ~~~~~~~~~~THIS IS TOO LARGE FOR MOST PYTHON VIRTUAL MACHINES~~~~~~~~~~
# # Large lists
# x, y = list(range(1000)), list(range(1000))
# print(f"{rec_addlists(x, y)} should be {list(2 * i for i in range(1000))}")  # Expected output: [0, 2, 4, ..., 1998]

# Lists with floating-point numbers
x, y = [1.5, 2.5, 3.5], [0.5, 1.5, 2.5]
print(f"{rec_addlists(x, y)} should be [2.0, 4.0, 6.0]")  # Expected output: [2.0, 4.0, 6.0]

# Lists with mixed types
x, y = [1, 2.5, 3], [4, 5.5, 6]
print(f"{rec_addlists(x, y)} should be [5, 8.0, 9]")  # Expected output: [5, 8.0, 9]
