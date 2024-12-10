def rec_oddsum(x):
    """
    Same restrictions apply. We need to return the total sum of ONLY the ODD numbers within the list (x).
    :param x: A list of numbers.
    :return: The sum of the ODD numbers in x.
    """
    if x == []:
        return 0
    head = x[0]
    tail = x[1:]
    forcedRecursion = rec_oddsum(tail)

    if head % 2 == 0:
        return forcedRecursion
    else:
        return head + rec_oddsum(tail)

# test code below provided by GPT
# Test cases for rec_oddsum(x)

# Base case: Empty list
x = []
print(f"{rec_oddsum(x)} should be 0")  # Expected output: 0

# Single-element list (odd number)
x = [5]
print(f"{rec_oddsum(x)} should be 5")  # Expected output: 5

# Single-element list (even number)
x = [4]
print(f"{rec_oddsum(x)} should be 0")  # Expected output: 0

# Multi-element list with mixed odd and even numbers
x = [1, 2, 3, 4, 5]
print(f"{rec_oddsum(x)} should be 9")  # Expected output: 9 (1 + 3 + 5)

# Multi-element list with all even numbers
x = [2, 4, 6, 8]
print(f"{rec_oddsum(x)} should be 0")  # Expected output: 0

# Multi-element list with all odd numbers
x = [1, 3, 5, 7]
print(f"{rec_oddsum(x)} should be 16")  # Expected output: 16 (1 + 3 + 5 + 7)

# Multi-element list with negative odd numbers
x = [-1, -3, -5]
print(f"{rec_oddsum(x)} should be -9")  # Expected output: -9 (-1 + -3 + -5)

# Multi-element list with a mix of positive and negative numbers
x = [1, -2, 3, -4, -5]
print(f"{rec_oddsum(x)} should be -1")  # Expected output: -1 (1 + 3 + -5)

# Large list
x = list(range(1, 101))  # List from 1 to 100
print(f"{rec_oddsum(x)} should be 2500")  # Expected output: 2500 (sum of all odd numbers from 1 to 100)

# List with a single zero
x = [0]
print(f"{rec_oddsum(x)} should be 0")  # Expected output: 0
