def rec_records(x):
    """
    Same restrictions as before. We need to see how many times the current element was bigger than all the previous elements.
    :param x: A list.
    :return: The total number of times the current element was bigger than all the previous elements.
    """

    if x == []:
        return 0

    head = x[0]
    tail = x[1:]

    forcedRecursion = rec_records(tail)

    if tail != [] and head < tail[0]:
        return forcedRecursion + 1
    else:
        return forcedRecursion

# test code below provided by GPT
# Test cases for rec_records(x)

# Base case: Empty list
x = []
print(f"{rec_records(x)} should be 0")  # Expected output: 0

# Single-element list
x = [5]
print(f"{rec_records(x)} should be 0")  # Expected output: 0 (the first element is not considered a record)

# Two-element list with no record
x = [5, 3]
print(f"{rec_records(x)} should be 0")  # Expected output: 0 (second element is not greater than the first)

# Two-element list with one record
x = [5, 6]
print(f"{rec_records(x)} should be 1")  # Expected output: 1 (6 is greater than 5)

# Multi-element list with increasing numbers
x = [1, 2, 3, 4, 5]
print(f"{rec_records(x)} should be 4")  # Expected output: 4 (2, 3, 4, 5 are records)

# Multi-element list with decreasing numbers
x = [5, 4, 3, 2, 1]
print(f"{rec_records(x)} should be 0")  # Expected output: 0 (no element is a record)

# Multi-element list with mixed numbers
x = [3, 5, 2, 7, 6, 8]
print(f"{rec_records(x)} should be 3")  # Expected output: 3 (5, 7, and 8 are records)

# Multi-element list with duplicates
x = [4, 4, 4, 4]
print(f"{rec_records(x)} should be 0")  # Expected output: 0 (no element is greater than the previous ones)

# Multi-element list with alternating highs and lows
x = [3, 5, 2, 6, 4, 7]
print(f"{rec_records(x)} should be 3")  # Expected output: 3 (5, 6, and 7 are records)

# Large list
x = list(range(1, 101))  # List from 1 to 100
print(f"{rec_records(x)} should be 99")  # Expected output: 99 (all elements after the first are records)

# List with negative and positive numbers
x = [-5, -3, -4, -2, 0, 1, 5, 3]
print(f"{rec_records(x)} should be 4")  # Expected output: 4 (-3, -2, 0, 5 are records)
