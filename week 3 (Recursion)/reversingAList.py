def rec_rev(x):
    """
    Same restrictions as before. We need to create a function that takes in a list (x) and returns a new list where each
    element is in reversed order. So x[0] would now be in x[-1]'s position and vice versa.
    :param x: A list.
    :return: A reversed list.
    """

    if x == []:
        return []

    head = x[0]
    tail = x[1:]

    forcedRecursion = rec_rev(tail)

    return forcedRecursion + [head]

# test code provided by GPT
# Test cases for rec_rev(x)

# Base case: Empty list
x = []
print(f"{rec_rev(x)} should be []")  # Expected output: []

# Single-element list
x = [1]
print(f"{rec_rev(x)} should be [1]")  # Expected output: [1]

# Two-element list
x = [1, 2]
print(f"{rec_rev(x)} should be [2, 1]")  # Expected output: [2, 1]

# Multi-element list with increasing numbers
x = [1, 2, 3, 4, 5]
print(f"{rec_rev(x)} should be [5, 4, 3, 2, 1]")  # Expected output: [5, 4, 3, 2, 1]

# Multi-element list with mixed numbers
x = [5, -3, 0, 7, -1]
print(f"{rec_rev(x)} should be [-1, 7, 0, -3, 5]")  # Expected output: [-1, 7, 0, -3, 5]

# Multi-element list with repeated elements
x = [1, 2, 2, 3, 3]
print(f"{rec_rev(x)} should be [3, 3, 2, 2, 1]")  # Expected output: [3, 3, 2, 2, 1]

# List with mixed data types
x = [1, "a", 3.5, True]
print(f"{rec_rev(x)} should be [True, 3.5, 'a', 1]")  # Expected output: [True, 3.5, 'a', 1]

# Large list
x = list(range(100))  # List from 0 to 99
expected = list(range(99, -1, -1))  # List from 99 to 0
print(f"{rec_rev(x)} should be {expected}")  # Expected output: reversed list of x

# List with a single repeated value
x = [5, 5, 5, 5]
print(f"{rec_rev(x)} should be [5, 5, 5, 5]")  # Expected output: [5, 5, 5, 5]

# List with nested lists
x = [[1, 2], [3, 4], [5, 6]]
print(f"{rec_rev(x)} should be [[5, 6], [3, 4], [1, 2]]")  # Expected output: reversed order of sublists
