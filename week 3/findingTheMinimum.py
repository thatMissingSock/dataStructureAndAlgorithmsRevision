def rec_min(x):
    """
    Same restrictions. You need to find the minimum of the list recursively.
    :param x: A list.
    :return: The smallest element of x.
    """

    head = x[0]
    tail = x[1:]

    if tail == []:
        return head

    minTail = rec_min(tail)

    if head < minTail:
        return head
    return minTail

# test code below
# Test cases for rec_min(x)

# Single-element list
x = [5]
print(f"{rec_min(x)} should be 5")  # Expected output: 5

# Multi-element list with positive numbers
x = [1, 2, 3, 4]
print(f"{rec_min(x)} should be 1")  # Expected output: 1

# Multi-element list with negative numbers
x = [-1, -2, -3, -4]
print(f"{rec_min(x)} should be -4")  # Expected output: -4

# Multi-element list with a mix of positive and negative numbers
x = [5, -1, 7, 0, -10]
print(f"{rec_min(x)} should be -10")  # Expected output: -10

# Multi-element list with duplicates
x = [3, 3, 3, 3]
print(f"{rec_min(x)} should be 3")  # Expected output: 3

# Multi-element list with a mix of integers and floats
x = [1.5, -2.5, 0, 3.5]
print(f"{rec_min(x)} should be -2.5")  # Expected output: -2.5

# List with a single negative element
x = [-42]
print(f"{rec_min(x)} should be -42")  # Expected output: -42

# Large list
x = list(range(100, -1, -1))  # List from 100 to 0
print(f"{rec_min(x)} should be 0")  # Expected output: 0
