def rec_prod(x):
    """
    We have the same restrictions (we can only look if its empty and if not then at the tail and head) but instead of
    checking what the length of the list is, we need to recursively find the product of each element in the list.
    :param x: A list
    :return: The product of all elements in x.
    """
    if x == []:
        return 1
    head = x[0]
    tail = x[1:]

    return head * rec_prod(tail)

# test code below provided by GPT
# Test cases for rec_prod(x)

# Base case: Empty list
x = []
print(f"{rec_prod(x)} should be 1")  # Expected output: 1

# Single-element list
x = [5]
print(f"{rec_prod(x)} should be 5")  # Expected output: 5

# Multi-element list with positive numbers
x = [1, 2, 3, 4]
print(f"{rec_prod(x)} should be 24")  # Expected output: 24

# Multi-element list with negative numbers
x = [-1, 2, -3]
print(f"{rec_prod(x)} should be 6")  # Expected output: 6

# Multi-element list with a zero
x = [1, 2, 0, 4]
print(f"{rec_prod(x)} should be 0")  # Expected output: 0

# Multi-element list with only ones
x = [1, 1, 1, 1]
print(f"{rec_prod(x)} should be 1")  # Expected output: 1

# Multi-element list with decimals
x = [0.5, 2, 4]
print(f"{rec_prod(x)} should be 4.0")  # Expected output: 4.0

# Multi-element list with a mix of integers and floats
x = [1.5, 2, -3]
print(f"{rec_prod(x)} should be -9.0")  # Expected output: -9.0

# Multi-element list with negative decimals
x = [-0.5, -2, 4]
print(f"{rec_prod(x)} should be 4.0")  # Expected output: 4.0

# Large list
x = list(range(1, 10))  # List from 1 to 9
print(f"{rec_prod(x)} should be 362880")  # Expected output: 362880

