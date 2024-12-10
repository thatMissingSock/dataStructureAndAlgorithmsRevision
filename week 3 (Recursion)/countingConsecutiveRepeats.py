def rec_reps(x):
    """
    Same restrictions as before. We need to return the number of times x[n] == x[n-1].
    :param x: A list.
    :return: The total amount of time instant repetition occurs within x.
    """
    if x == []:
        return 0
    head = x[0]
    tail = x[1:]

    forcedRecursion = rec_reps(tail)

    if tail != [] and head == tail[0]:
        return forcedRecursion + 1
    else:
        return forcedRecursion

# test code below as provided by GPT
# Test cases for rec_reps(x)

# Base case: Empty list
x = []
print(f"{rec_reps(x)} should be 0")  # Expected output: 0

# Single-element list
x = [5]
print(f"{rec_reps(x)} should be 0")  # Expected output: 0

# Two-element list with no repeats
x = [5, 6]
print(f"{rec_reps(x)} should be 0")  # Expected output: 0

# Two-element list with one repeat
x = [5, 5]
print(f"{rec_reps(x)} should be 1")  # Expected output: 1

# Multi-element list with consecutive repeats
x = [1, 1, 1, 2, 2, 3, 3, 3]
print(f"{rec_reps(x)} should be 5")  # Expected output: 6 (1->1, 1->1, 2->2, 3->3, 3->3)

# Multi-element list with no consecutive repeats
x = [1, 2, 3, 4, 5]
print(f"{rec_reps(x)} should be 0")  # Expected output: 0

# Multi-element list with alternating repeats
x = [1, 1, 2, 2, 3, 3, 4, 4]
print(f"{rec_reps(x)} should be 4")  # Expected output: 4 (1->1, 2->2, 3->3, 4->4)

# Multi-element list with all elements the same
x = [7, 7, 7, 7, 7]
print(f"{rec_reps(x)} should be 4")  # Expected output: 4 (7->7, 7->7, 7->7, 7->7)

# Large list with a pattern
x = [1, 1, 2, 2] * 100  # Pattern repeated 100 times
print(f"{rec_reps(x)} should be 200")  # Expected output: 200 (each pattern contributes 2 repeats)

# List with mixed data types
x = [1, "a", "a", 2, 3, 3]
print(f"{rec_reps(x)} should be 2")  # Expected output: 2 ("a"->"a", 3->3)
