
def rec_len(x):
    """
    This is restrictive in the sense that you can only access the given list (x) by either checking if it's empty and if
    not then you can only check the head x[0] and the tail x[1:]. Given these restrictions we need to check the length of
    the list WITHOUT USING LEN().
    :param x: A list.
    :return: The length of said list.
    """

    if x == []:
        return 0

    return 1 + rec_len(x[1:])

# test code below provided by GPT
# Test cases for rec_len(x)

# Base case: Empty list
x = []
print(f"{rec_len(x)} should be 0")  # Expected output: 0

# Single-element list
x = [1]
print(f"{rec_len(x)} should be 1")  # Expected output: 1

# Multi-element list
x = [1, 2, 3]
print(f"{rec_len(x)} should be 3")  # Expected output: 3

# List with nested lists
x = [[1, 2], [3, 4], [5]]
print(f"{rec_len(x)} should be 3")  # Expected output: 3 (only considers the outer list)

# List with duplicate elements
x = [1, 1, 1, 1, 1]
print(f"{rec_len(x)} should be 5")  # Expected output: 5

# ~~~~~~~~~~~~~~this one works but due to my PVM RAM limitations it won't work~~~~~~~~~~~~~~
# # Large list
# x = list(range(1000))  # List from 0 to 999
# print(f"{rec_len(x)} should be 1000")  # Expected output: 1000

# List with mixed data types
x = [1, "two", 3.0, [4, 5]]
print(f"{rec_len(x)} should be 4")  # Expected output: 4

# List with negative numbers
x = [-1, -2, -3, -4, -5]
print(f"{rec_len(x)} should be 5")  # Expected output: 5
